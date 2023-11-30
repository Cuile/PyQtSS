from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QWidget, QApplication, QMainWindow
from PySide6.QtGui import QIcon, QAction
from resources import res_rc  # 由pyside6-rcc生成的资源文件  # noqa: F401


# 系统托盘
class SysTrayWidget(QWidget):
    __tray_icon: QSystemTrayIcon
    __tray_menu: QMenu
    __tray_menu_action: list = []

    def __del__(self) -> None:
        pass

    def __init__(
        self,
        app: QApplication,
        window: QMainWindow,
        ui: object = None,
    ) -> None:
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
        self.add_tray_menu_action("主界面", self.show_userinterface)
        self.__tray_menu.addSeparator()
        self.add_tray_menu_action("关闭代理模式", self.show_userinterface)
        self.add_tray_menu_action("网络直通模式", self.show_userinterface)
        self.add_tray_menu_action("软件PAC模式", self.show_userinterface)
        self.add_tray_menu_action("系统PAC模式", self.show_userinterface)
        self.add_tray_menu_action("全局代理模式", self.show_userinterface)
        self.__tray_menu.addSeparator()
        self.add_tray_menu_action("查看日志", self.show_userinterface)
        self.add_tray_menu_action("帮助", self.show_userinterface)
        self.add_tray_menu_action("关于", self.show_userinterface)
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

    def add_tray_menu_action(
        self, text: str = "empty", callback: object = None
    ) -> None:
        a = QAction(text, self)
        a.triggered.connect(callback)
        self.__tray_menu.addAction(a)
        self.__tray_menu_action.append(a)

    def quit(self) -> None:
        # 真正的退出
        self.__app.exit()

    def show_userinterface(self) -> None:
        # self.__window.show()
        pass

    def hide_userinterface(self) -> None:
        # self.__window.hide()
        pass
