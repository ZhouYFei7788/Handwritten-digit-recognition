# paint_label.py
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPainter, QPen

class PaintLabel(QLabel):
    """绘制鼠标路径"""
    path_updated = pyqtSignal(list)  # Signal to emit the mouse path

    def __init__(self, parent=None):
        super().__init__(parent)
        self.mouse_path = []  # 存储鼠标路径

    def mouseMoveEvent(self, event):
        """移动鼠标事件"""
        self.mouse_path.append(event.pos())
        self.update()
        self.path_updated.emit(self.mouse_path)  # Emit the updated path

    def mouseReleaseEvent(self, event):
        """释放鼠标事件"""
        self.update()
        self.path_updated.emit(self.mouse_path)  # Emit the updated path

    def paintEvent(self, event):
        """绘制事件"""
        super().paintEvent(event)
        if self.mouse_path:
            painter = QPainter(self)
            pen = QPen(Qt.black, 2)
            painter.setPen(pen)
            for i in range(len(self.mouse_path) - 1):
                painter.drawLine(self.mouse_path[i], self.mouse_path[i + 1])

    def get_mouse_path(self):
        """获取鼠标路径"""
        return self.mouse_path