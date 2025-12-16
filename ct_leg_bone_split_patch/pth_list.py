import os
import traceback
import time
from .download import download_file
DIRNOW = os.path.dirname(os.path.abspath(__file__))

class NetworkError(Exception):
    def __init__(self, msg):
        super().__init__(self.msg)
        self.msg = msg

PTH_LIST = {
    os.path.join(DIRNOW, "model", "unet_model_part_000.pth"): 
        "https://github.com/GGN-2015/ct_leg_bone_split_patch/releases/download/pth_binary/unet_model_part_000.pth",
    os.path.join(DIRNOW, "model", "unet_model_part_001.pth"): 
        "https://github.com/GGN-2015/ct_leg_bone_split_patch/releases/download/pth_binary/unet_model_part_001.pth",
    os.path.join(DIRNOW, "model", "unet_model_part_002.pth"): 
        "https://github.com/GGN-2015/ct_leg_bone_split_patch/releases/download/pth_binary/unet_model_part_002.pth",
    os.path.join(DIRNOW, "model", "unet_model_part_003.pth"): 
        "https://github.com/GGN-2015/ct_leg_bone_split_patch/releases/download/pth_binary/unet_model_part_003.pth",
}

def download_all_pth(MAX_TRY:int=3):
    for filepath in PTH_LIST:
        file_url = PTH_LIST[filepath]

        if not os.path.isfile(filepath):
            fail_cnt = 0
            suc=False
            while fail_cnt < MAX_TRY:
                try:
                    print(f"downloading {file_url}")
                    download_file(file_url, filepath)
                    suc = True
                except:
                    fail_cnt += 1
                    print(f"downloading {file_url} failed, fail_cnt: {fail_cnt}")
                    traceback.print_exc()
                    time.sleep(3)
                if suc:
                    break
        
        if fail_cnt >= MAX_TRY and not suc:
            raise NetworkError("can not download file from {file_url}")
