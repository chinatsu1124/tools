from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QStatusBar
from ui_main_window import Ui_mainWindow
import os

class DragDropLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setAcceptDrops(True)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            file_path = urls[0].toLocalFile()
            if os.path.exists(file_path):
                self.setText(file_path)
                if self.window().statusBar():
                    self.window().statusBar().showMessage(f"已添加: {file_path}")
                event.acceptProposedAction()
            else:
                event.ignore()

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("拖放测试")
        self.resize(400, 100)
        self.setAcceptDrops(True)
        
        # 创建状态栏
        self.statusBar().showMessage("请拖放文件到输入框")
        
        # 创建自定义输入框
        self.line_edit = DragDropLineEdit(self)
        self.setCentralWidget(self.line_edit)

if __name__ == "__main__":
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec()