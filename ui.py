from PyQt5 import QtCore, QtGui, QtWidgets
from PaintLabel import PaintLabel  # 导入 PaintLabel 类

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 595)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 311, 241))
        self.frame.setMaximumSize(QtCore.QSize(16777212, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = PaintLabel(self.frame)  # 使用 PaintLabel
        self.label_2.setGeometry(QtCore.QRect(20, 30, 291, 201))
        self.label_2.setStyleSheet("QLabel {\n"
"    border: 2px solid black;   /* 黑色边框，2像素宽 */\n"
"    background-color: white;   /* 白色背景 */\n"
"}\n"
"")

        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 240, 291, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.progressBar_1 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_1.setProperty("value", 0)
        self.verticalLayout_2.setObjectName("progressBar_1")
        self.verticalLayout_2.addWidget(self.progressBar_1)

        self.progressBar_2 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout_2.addWidget(self.progressBar_2)

        self.progressBar_3 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout_2.addWidget(self.progressBar_3)

        self.progressBar_4 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout_2.addWidget(self.progressBar_4)

        self.progressBar_5 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout_2.addWidget(self.progressBar_5)

        self.progressBar_6 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_6.setMinimum(0)
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setTextVisible(True)
        self.progressBar_6.setObjectName("progressBar_6")
        self.verticalLayout_2.addWidget(self.progressBar_6)

        self.progressBar_7 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setObjectName("progressBar_7")
        self.verticalLayout_2.addWidget(self.progressBar_7)

        self.progressBar_8 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_8.setProperty("value", 0)
        self.progressBar_8.setObjectName("progressBar_8")
        self.verticalLayout_2.addWidget(self.progressBar_8)

        self.progressBar_9 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_9.setProperty("value", 0)
        self.progressBar_9.setObjectName("progressBar_9")
        self.verticalLayout_2.addWidget(self.progressBar_9)

        self.progressBar_0 = QtWidgets.QProgressBar(self.verticalLayoutWidget_2)
        self.progressBar_0.setProperty("value", 0)
        self.progressBar_0.setObjectName("progressBar_0")
        self.verticalLayout_2.addWidget(self.progressBar_0)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 530, 200, 50))
        self.pushButton.setObjectName("pushButton")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 70, 431, 431))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    background-color: #2e2e2e;    /* 深色背景 */\n"
"    color: #ffffff;               /* 白色文本 */\n"
"    border-radius: 10px;          /* 圆角 */\n"
"    padding: 10px;                /* 内边距，避免文字太靠近边框 */\n"
"    border: 2px solid #4a4a4a;    /* 边框颜色和宽度 */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #2e2e2e;    /* 滚动条背景颜色 */\n"
"    width: 15px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5c5c5c;    /* 滚动条滑块颜色 */\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 20, 91, 41))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.scaleUi(MainWindow, 1.5)  # Scale the UI by 1.5 times
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "此处书写:"))
        self.progressBar_1.setFormat(_translate("MainWindow", "1:相似度%p%"))
        self.progressBar_2.setFormat(_translate("MainWindow", "2:相似度%p%"))
        self.progressBar_3.setFormat(_translate("MainWindow", "3:相似度%p%"))
        self.progressBar_4.setFormat(_translate("MainWindow", "4:相似度%p%"))
        self.progressBar_5.setFormat(_translate("MainWindow", "5:相似度%p%"))
        self.progressBar_6.setFormat(_translate("MainWindow", "6:相似度%p%"))
        self.progressBar_7.setFormat(_translate("MainWindow", "7:相似度%p%"))
        self.progressBar_8.setFormat(_translate("MainWindow", "8:相似度%p%"))
        self.progressBar_9.setFormat(_translate("MainWindow", "9:相似度%p%"))
        self.progressBar_0.setFormat(_translate("MainWindow", "0:相似度%p%"))
        self.pushButton.setText(_translate("MainWindow", "选择模型"))
        self.label_3.setText(_translate("MainWindow", "推理值:"))

    def scaleUi(self, MainWindow, scale_factor):
        MainWindow.resize(MainWindow.width() * scale_factor, MainWindow.height() * scale_factor)
        for widget in MainWindow.findChildren(QtWidgets.QWidget):
            widget.resize(widget.width() * scale_factor, widget.height() * scale_factor)
            widget.move(widget.x() * scale_factor, widget.y() * scale_factor)