from PySide6.QtWidgets import QApplication, QMainWindow
import rename_modules as rename
from ui_main_window import Ui_mainWindow
import aria2_lib as aria2

class Tools(QMainWindow):
    def __init__(self):
        super().__init__()  # 初始化父类
        # 加载界面
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # 绑定信号
        rename.signal.progress.connect(self.ui.statusbar.showMessage)
        aria2.signal.progress.connect(self.ui.statusbar.showMessage)
        # 绑定按钮
        self.ui.video_rename_button.clicked.connect(self.rename_series)
        self.ui.anime_rename_button.clicked.connect(self.rename_animes)
        self.ui.aria2_button.clicked.connect(self.aria2_del)

    def rename_series(self):
        path = self.ui.rename_folder_path.text()
        series_name = self.ui.series_name.text()
        season = self.ui.season.text()
        year = self.ui.year.text()
        re_str = self.ui.re.text()
        if all([path, series_name, season, year, re_str]):
            rename.rename_series(path, series_name, season, year, re_str)
        else:
            self.ui.statusbar.showMessage("请填写完整信息")

    def rename_animes(self):
        path = self.ui.rename_folder_path.text()
        if path:
            rename.rename_animes(path)
        else:
            self.ui.statusbar.showMessage("请先选择文件夹路径")
    
    def aria2_del(self):
        keyword = self.ui.aria2_keyword.text()
        if keyword:
            aria2.batch_del_downloads(keyword)
        else:
            self.ui.statusbar.showMessage("请填写关键字")

app = QApplication([])
window = Tools()
window.show()
app.exec()