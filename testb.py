from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
import os

class DragDropLineEditWithAcceptDrops(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)  # 设置接受拖放
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.setText(urls[0].toLocalFile())
            event.acceptProposedAction()

class DragDropLineEditWithoutAcceptDrops(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 不设置 setAcceptDrops
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()
            
    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.setText(urls[0].toLocalFile())
            event.acceptProposedAction()

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("拖放测试")
        
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel("设置 setAcceptDrops:"))
        layout.addWidget(DragDropLineEditWithAcceptDrops())
        
        layout.addWidget(QLabel("不设置 setAcceptDrops:"))
        layout.addWidget(DragDropLineEditWithoutAcceptDrops())
        
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = TestWindow()
    window.show()
    app.exec()