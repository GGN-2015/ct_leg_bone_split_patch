import urllib.request
import os

def download_file(url, save_path:str):
    # 确保保存文件夹存在，不存在则创建
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    urllib.request.urlretrieve(url, save_path)
