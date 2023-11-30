from config import settings as set
from PySide6.QtCore import QProcess


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
