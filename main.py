import sys
import torch
import torch.nn as nn
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QLineEdit, QProgressBar
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from ui import Ui_MainWindow  # 确保你有这个导入
from dect import Net  # 假设模型类定义在 train.py 中

# 定义设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

import sys
import torch
import torch.nn as nn
import cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QLineEdit, QProgressBar
from PyQt5.QtCore import pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QPainter, QPen
from ui import Ui_MainWindow  # 确保你有这个导入
from dect import Net  # 假设模型类定义在 train.py 中

# 定义设备
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class PaintLabel(QLabel):
    """绘制鼠标路径"""
    path_updated = pyqtSignal(list)  # 信号以发出鼠标路径
    mouse_released = pyqtSignal()  # 鼠标释放信号

    def __init__(self, parent=None):
        super().__init__(parent)
        self.paths = []  # 存储多个绘制路径
        self.current_path = []  # 存储当前的绘制路径
        self.drawing = False  # 标记当前是否在绘制中

    def mousePressEvent(self, event):
        """按下鼠标事件"""
        if event.button() == Qt.LeftButton:
            self.drawing = True  # 设置为绘制状态
            self.current_path = [event.pos()]  # 初始化当前路径
            self.update()  # 更新界面

    def mouseMoveEvent(self, event):
        """移动鼠标事件"""
        if self.drawing:  # 仅在绘制状态下添加路径
            self.current_path.append(event.pos())  # 添加当前鼠标位置
            self.update()  # 更新界面

            # 添加实时推理逻辑
            input_tensor = self.parent().paths_to_tensor()  # 获取绘制路径对应的张量
            if input_tensor is not None:
                similarity_scores = self.parent().make_prediction(input_tensor)  # 进行推理
                print(f"实时预测结果: {similarity_scores}")  # 打印预测结果
                self.parent().update_progress_bars(similarity_scores)  # 更新进度条

    def mouseReleaseEvent(self, event):
        """释放鼠标事件"""
        self.drawing = False  # 结束绘制状态
        self.current_path.append(event.pos())  # 添加释放位置
        self.paths.append(self.current_path)  # 将当前路径添加到路径列表
        self.mouse_released.emit()  # 发出鼠标释放信号
        self.update()  # 请求重绘


        # 添加推理逻辑
        input_tensor = self.parent().paths_to_tensor()  # 获取绘制路径对应的张量
        if input_tensor is not None:
            similarity_scores = self.parent().make_prediction(input_tensor)  # 进行推理
            print(f"预测结果: {similarity_scores}")  # 打印预测结果
            self.parent().update_progress_bars(similarity_scores)  # 更新进度条

    def paintEvent(self, event):
        """绘制事件"""
        super().paintEvent(event)
        painter = QPainter(self)
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)

        # 绘制所有路径
        for path in self.paths:
            for i in range(len(path) - 1):
                painter.drawLine(path[i], path[i + 1])

        # 绘制当前路径（如果在绘制中）
        if self.current_path:
            for i in range(len(self.current_path) - 1):
                painter.drawLine(self.current_path[i], self.current_path[i + 1])

    def clear_drawing(self):
        """清空画板"""
        self.paths.clear()  # 清空所有路径
        self.current_path.clear()  # 清空当前路径
        self.update()  # 更新界面以反映清空

class MainWindow(QMainWindow, Ui_MainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.file_name = ""  # 初始化文件名
        self.model = Net().to(device)  # 创建模型实例并移动到设备
        self.model_loaded = False  # 添加模型加载标志
        self.paint_label = PaintLabel(self)
        self.paint_label.setGeometry(50, 50, 400, 300)  # 设置位置和大小

        self.paint_label.path_updated.connect(self.on_path_updated)  # 连接信号
        self.paint_label.mouse_released.connect(self.start_timer)  # 连接鼠标释放信号

        self.timer = QTimer(self)  # 创建定时器
        self.timer.timeout.connect(self.clear_drawing)  # 连接定时器超时信号
        self.image = None  # 初始化图像张量

    def initUI(self):
        """初始化 UI"""
        self.pushButton.clicked.connect(self.load_model)  # 连接信号

    def load_model(self):
        """打开文件对话框选择模型文件"""
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择模型文件", "", "模型文件 (*.pth);;所有文件 (*)", options=options)

        if file_name:
            self.pushButton.setText("加载模型: " + file_name.split('/')[-1])  # 显示文件名
            try:
                self.model.load_state_dict(torch.load(file_name, map_location=device))  # 加载模型权重
                print(f"模型已加载: {file_name}")
            except Exception as e:
                print(f"加载模型失败: {e}")  # 捕获并打印错误信息

    def on_path_updated(self, mouse_path):
        """处理鼠标路径更新事件"""
        if not mouse_path:
            print("鼠标路径已清空")
        else:
            print("当前鼠标路径:", mouse_path)

    def start_timer(self):
        """启动定时器"""
        self.timer.start(2000)  # 启动定时器，2秒后清空画板

    def clear_drawing(self):
        """清空画板"""
        self.paint_label.clear_drawing()  # 清空绘图
        print("鼠标路径已清空")  # 输出路径已清空的信息
        self.timer.stop()  # 停止定时器

    def paths_to_tensor(self):
        """将绘制路径转换为张量"""
        try:
            if not self.paint_label.paths:
                # print("没有绘制路径")
                return None

            height, width = 28, 28
            image = np.zeros((height, width), dtype=np.uint8)

            for path in self.paint_label.paths:
                for point in path:
                    x = int(point.x() * width // self.paint_label.width())
                    y = int(point.y() * height // self.paint_label.height())

                    if 0 <= x < width and 0 <= y < height:
                        image[y, x] = 255  # 设置像素值

            # 转换为张量并归一化
            return torch.from_numpy(image).unsqueeze(0).unsqueeze(0).float() / 255.0

        except Exception as e:
            print(f"发生错误: {e}")  # 捕获并打印异常信息
            return None

    def make_prediction(self, input_tensor):
        """根据输入数据进行推理预测"""
        self.model.eval()
        with torch.no_grad():
            input_tensor = input_tensor.to(device)
            output = self.model(input_tensor)
            probabilities = torch.softmax(output, dim=1)
        return probabilities.squeeze().cpu().numpy()  # 返回所有类别的相似度分数

    def update_progress_bars(self, similarity_scores):
        """更新进度条的显示"""
        progress_bars = [
            self.progressBar_0,
            self.progressBar_1,
            self.progressBar_2,
            self.progressBar_3,
            self.progressBar_4,
            self.progressBar_5,
            self.progressBar_6,
            self.progressBar_7,
            self.progressBar_8,
            self.progressBar_9,
        ]

        # 更新进度条
        for i, score in enumerate(similarity_scores):
            if i < len(progress_bars):  # 确保索引不越界
                progress_bars[i].setValue(score * 100)  # 将分数转为百分比形式
        similarity_scores = np.array(similarity_scores)
        # 计算最大相似度分数及其索引
        max_score = max(similarity_scores)
        max_index = similarity_scores.argmax()  # 获取最大值的索引
        # 归一化
        normalized_score = (max_score - min(similarity_scores)) / (max(similarity_scores) - min(similarity_scores))

        # 将归一化值映射到0到9之间
        mapped_score = int(normalized_score * 9)
        self.label_3.setText(f"推理值: {mapped_score}")  # 这里是整数值


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())