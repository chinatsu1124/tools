import shutil, os, re
from PySide6.QtCore import QObject, Signal

ANIME_PATTERN = r'\[.*?\]\[.*?\](.*)\.chs\.mp4'

class RenameSignal(QObject):
    progress = Signal(str)     # 用于发送状态信息的信号

signal = RenameSignal()

# 添加路径验证
def rename_animes(path):
    if not os.path.exists(path):
        signal.progress.emit(f"错误：路径 {path} 不存在")
        return 0
        
    file_num = 0
    pattern = ANIME_PATTERN
    
    for file_name in os.listdir(path):
        video_path = os.path.join(path, file_name)
        if is_valid_video_file(video_path):
            match = re.search(pattern, file_name)
            if match:
                anime_name = match.group(1)
                video_extension = os.path.splitext(file_name)[-1]
                new_file_name = f'{anime_name}{video_extension}'
                new_file_path = os.path.join(path, new_file_name)
                shutil.move(video_path, new_file_path)
                file_num += 1
                print(f'成功重命名为{new_file_name}。')
            else:
                print(f'{file_name}未匹配模式，跳过。')
        else:
            print(f'{file_name}非视频文件, 跳过。')
    signal.progress.emit(f'共重命名了{file_num}个视频')
    return file_num

def rename_series(path, series_name, season, year):
    file_num = 0
    for file_name in os.listdir(path):
        video_path = os.path.join(path, file_name)
        if is_valid_video_file(video_path):
            try:
                episode = re.search(r'E(\d{2})', file_name, re.IGNORECASE).group(1)
                video_season_path = os.path.join(path, f'{series_name} ({year})', f'Season {season}')
                if not os.path.exists(video_season_path):
                    os.makedirs(video_season_path)
                video_extension = os.path.splitext(video_path)[-1]
                if video_extension == '.srt':
                    new_file_name = f'{series_name} S0{season}E{episode}.chs{video_extension}'
                else:
                    new_file_name = f'{series_name} S0{season}E{episode}{video_extension}'
                new_file_path = os.path.join(video_season_path, new_file_name)
                shutil.move(video_path, new_file_path)
                file_num += 1
                print(f'成功重命名为{new_file_name}。')
            except AttributeError:
                print(f'{file_name}未标明集数, 跳过。')
        else:
            print(f'{file_name}非视频文件, 跳过。')
    signal.progress.emit(f'成功重命名{file_num}个文件。')
    return file_num

def is_valid_video_file(file_path):
    video_extensions = ['.mp4', '.mkv', '.avi']
    return os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in video_extensions)