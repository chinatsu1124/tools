from PySide6.QtCore import QObject, Signal

class StatusSignal(QObject):
    progress = Signal(str)     # 用于发送状态信息的信号