from config import settings as set
from PySide6.QtCore import QProcess
# 在调试里看系统路径
# import sys, os.path


# 主程守护进程
class supervisor:
    def __init__(self) -> None:
        # 读取配置文件
        sup = set.supervisor
        daemon = QProcess()
        if daemon.startDetached(sup.bin, [sup.args, sup.conf]):
            print("supervisor start success.")
        else:
            print("supervisor start fail.")
