import os
import cv2
import shutil
from tqdm.auto import tqdm

train_data_path = 'F:/Data/super/train'
train_hr_file_list = os.listdir(train_data_path+'/hr')

edit_data_path = 'F:/train'
select_valid_unit = 90
count_file = 0

for filename in tqdm(train_hr_file_list):
    count_file += 1
    if count_file%select_valid_unit == 0:
        shutil.copy(train_data_path + '/hr/' +filename, edit_data_path + '/valid/hr/' +filename)
        shutil.copy(train_data_path + '/lr/' + filename, edit_data_path + '/valid/lr/' + filename)
    else:
        shutil.copy(train_data_path + '/hr/' +filename, edit_data_path + '/train/hr/' +filename)
        shutil.copy(train_data_path + '/lr/' + filename, edit_data_path + '/train/lr/' + filename)





