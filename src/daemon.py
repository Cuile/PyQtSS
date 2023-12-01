from config import settings as set
from PySide6.QtCore import QProcess, QProcessEnvironment
import os.path


# 主程守护进程
class supervisor:
    def __init__(self) -> None:
        # 读取配置文件
        sup = set.supervisor
        # 将bin目录添加到系统路径，传给守护进程
        env = QProcessEnvironment.systemEnvironment()
        path = env.value("PATH").split(";")
        path.append(os.path.abspath("."))
        env.insert("PATH", ";".join(path))
        env.insert("PYQTSS_ROOT", os.path.abspath("."))
        # 启动守护进程
        daemon = QProcess()
        daemon.setProcessEnvironment(env)
        daemon.setProgram(sup.bin)
        daemon.setArguments([sup.args, sup.conf])
        daemon.setWorkingDirectory(os.path.abspath("."))
        daemon.startDetached()
