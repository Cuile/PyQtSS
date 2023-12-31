import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from sysTray import SysTrayWidget
# import ui_untitled


class MainWindow(QMainWindow):
    # 继承一个QMainWindow，点右上角不会退出
    def __init__(self):
        QMainWindow.__init__(self)

    def closeEvent(self, event):
        # 忽略退出事件，而是隐藏到托盘
        event.ignore()
        self.hide()


if __name__ == "__main__":
    # 初始化应用和窗口
    app = QApplication(sys.argv)
    # win = MainWindow()

    # 载入界面
    # ui = ui_untitled.Ui_MainWindow()
    # ui.setupUi(win)

    # 创建系统托盘项目
    # tray = MySysTrayWidget(app=app, window=win, ui=ui)
    tray = SysTrayWidget(app=app, window=QMainWindow())

    # 显示窗口
    # win.show()

    # 运行应用
    sys.exit(app.exec())
