import os
import traceback
import time
from .download import download_file
DIRNOW = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(DIRNOW, "model")
MRI_MODEL_PATH = os.path.join(DIRNOW, "mri_model")

class NetworkError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

PTH_LIST = {
    os.path.join(MODEL_PATH, f"unet_model_part_00{i:01d}.pth"): 
        f"https://github.com/GGN-2015/ct_leg_bone_split_patch/releases/download/pth_binary/unet_model_part_00{i:01d}.pth"
    for i in range(0, 3 + 1)
}

PTH_LIST.update({
    os.path.join(MRI_MODEL_PATH, f"mri_best_model_a{chr(i)}.pth"): 
        f"https://github.com/GGN-2015/ct_leg_bone_split_patch/releases/download/mri_pth_binary/mri_best_model_a{chr(i)}.pth"
    for i in range(ord('a'), ord('l') + 1)
})

def download_all_pth(MAX_TRY:int=5):
    print(f"\033[1;33mdownloading {len(PTH_LIST)} files ...\033[0m")
    for filepath in PTH_LIST:
        file_url = PTH_LIST[filepath]

        fail_cnt = 0
        suc=False
        if not os.path.isfile(filepath):
            while fail_cnt < MAX_TRY:
                try:
                    print(f"\033[1;33downloading {file_url} ...\033[0m")
                    download_file(file_url, filepath)
                    suc = True
                    print(f"\033[1;32downloading {file_url} successfully\033[0m")
                except:
                    fail_cnt += 1
                    print(f"\033[1;33downloading {file_url} failed, fail_cnt: {fail_cnt} \033[0m")
                    traceback.print_exc()
                    time.sleep(3)
                if suc:
                    break
        else:
            suc=True
        
        if fail_cnt >= MAX_TRY and not suc:
            raise NetworkError(f"can not download file from {file_url}")
