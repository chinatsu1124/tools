from PySide6.QtWidgets import QLineEdit

class DragDropLineEdit(QLineEdit):
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