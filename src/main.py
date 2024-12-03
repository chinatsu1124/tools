# src/main.py
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
import rename_modules as rename
import os

uiLoader = QUiLoader()

class Tools:
    def __init__(self):
        # 加载界面
        self.ui = uiLoader.load('src/main_window.ui')
        self.ui.setAcceptDrops(True)  # 启用拖放

        # 绑定信号
        rename.signal.progress.connect(self.ui.statusbar.showMessage)
        # 绑定按钮
        self.ui.video_rename_button.clicked.connect(self.rename_series)
        self.ui.anime_rename_button.clicked.connect(self.rename_animes)

    def dragEnterEvent(self, event):
        # 接受拖入事件
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        # 处理拖放事件，获取文件夹路径并更新到输入框
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if os.path.isdir(file_path):
                self.ui.rename_folder_path.setText(file_path)
                self.ui.statusbar.showMessage(f"已选择文件夹: {file_path}")
                break
        event.acceptProposedAction()

    def rename_series(self):
        path = self.ui.rename_folder_path.text()
        series_name = self.ui.series_name.text()
        season = self.ui.season.text()
        year = self.ui.year.text()
        if all([path, series_name, season, year]):
            rename.rename_series(path, series_name, season, year)
        else:
            self.ui.statusbar.showMessage("请填写完整信息")

    def rename_animes(self):
        path = self.ui.rename_folder_path.text()
        if path:
            rename.rename_animes(path)
        else:
            self.ui.statusbar.showMessage("请先选择文件夹路径")

app = QApplication([])
tools = Tools()
tools.ui.show()
app.exec()