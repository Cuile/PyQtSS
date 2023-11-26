from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QIcon, QAction
import res_rc  # 由pyside6-rcc生成的资源文件  # noqa: F401


class SysTrayWidget(QWidget):
    __tray_icon: object = None
    __tray_menu: object = None
    __tray_menu_action: list = []

    def __del__(self):
        pass

    def __init__(self, ui: object = None, app: object = None, window: object = None):
        # 必须调用，否则信号系统无法启用
        QWidget.__init__(self)

        # 配置系统托盘图标
        self.__tray_icon = QSystemTrayIcon(self)
        self.__tray_icon.setIcon(QIcon(":/icons/sysTrayIcon.svg"))

        # 显示托盘
        # 一定要放在其它配置之前
        self.__tray_icon.show()

        # 配置托盘图标提示
        self.__tray_icon.setToolTip("PyQtSS")

        # 创建托盘的右键菜单
        self.__tray_menu = QMenu(self)
        self.add_tray_menu_action("显示主界面", self.show_userinterface)
        self.__tray_menu.addSeparator()
        self.add_tray_menu_action("退出", self.quit)
        # 把tpMenu设定为托盘的右键菜单
        self.__tray_icon.setContextMenu(self.__tray_menu)

        # 私有变量
        # self.__ui = ui
        self.__app = app
        # self.__window = window
        # self.__ui.setupUi(self.__window)

        # 连接信号
        # self.__ui.pushButton.clicked.connect(self.hide_userinterface)

        # 默认隐藏界面
        self.hide_userinterface()

    def add_tray_menu_action(self, text: str = "empty", callback: object = None):
        a = QAction(text, self)
        a.triggered.connect(callback)
        self.__tray_menu.addAction(a)
        self.__tray_menu_action.append(a)

    def quit(self):
        # 真正的退出
        self.__app.exit()

    def show_userinterface(self):
        # self.__window.show()
        pass

    def hide_userinterface(self):
        # self.__window.hide()
        pass
