from config import settings as set
from PySide6.QtCore import QProcess, QProcessEnvironment
import os.path
from xmlrpc.client import ServerProxy


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
        # 设置守护进程
        self.daemon = QProcess()
        self.daemon.setProcessEnvironment(env)
        self.daemon.setProgram(sup.bin)
        self.daemon.setArguments([sup.args, sup.conf])
        self.daemon.setWorkingDirectory(os.path.abspath("."))

    def start(self) -> bool:
        if self.daemon.startDetached():
            print("supervisor start success.")
            return True
        print("supervisor start fail.")
        return False


# 守护进程RPC
class rpc:
    def __init__(self) -> None:
        # 设置 XML-RPC
        self.rpc = ServerProxy("http://localhost:9001/RPC2")
