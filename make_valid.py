import os
import shutil
from tqdm.auto import tqdm

train_data_path = 'D:/Deep/super'
edit_data_path = './data'

train_hr_file_list = os.listdir(train_data_path+'/train/hr')

def createFolder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


createFolder(edit_data_path+'/train')
createFolder(edit_data_path+'/train/hr')
createFolder(edit_data_path+'/train/lr')
createFolder(edit_data_path+'/valid')
createFolder(edit_data_path+'/valid/hr')
createFolder(edit_data_path+'/valid/lr')


select_valid_unit = 90
count_file = 0

for filename in tqdm(train_hr_file_list):
    count_file += 1
    if count_file%select_valid_unit == 0:
        shutil.copy(train_data_path + '/train/hr/' +filename, edit_data_path + '/valid/hr/' +filename)
        shutil.copy(train_data_path + '/train/lr/' + filename, edit_data_path + '/valid/lr/' + filename)
    else:
        shutil.copy(train_data_path + '/train/hr/' +filename, edit_data_path + '/train/hr/' +filename)
        shutil.copy(train_data_path + '/train/lr/' + filename, edit_data_path + '/train/lr/' + filename)





