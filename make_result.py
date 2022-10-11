import os
import cv2
import zipfile
from tqdm.auto import tqdm

#result_dir = 'C:/Data/result'
result_dir ='D:/Deep/Hat/results/HAT-L_SRx4_ImageNet-pretrain/visualization/Set5'
result_output_dir = 'D:/Data/result_output'
result_image_list = []

file_list = os.listdir(result_dir)
new_file_list = []
for filename in file_list:
    new_filename= filename.replace('_HAT-L_SRx4_ImageNet-pretrain', '')
    print(new_filename)
    new_file_list.append(new_filename)
    print('Read '+result_dir+'/'+filename)
    img = cv2.imread(result_dir+'/'+filename)
    result_image_list.append(img)


os.makedirs(result_output_dir+'/submission', exist_ok=True)
os.chdir(result_output_dir+"/submission/")
sub_output_path=result_output_dir+"/submission/"
sub_imgs = []
for path, pred_img in tqdm(zip(new_file_list, result_image_list)):
    cv2.imwrite(sub_output_path+'/'+path, pred_img)
    sub_imgs.append(path)
submission = zipfile.ZipFile(sub_output_path+"/submission.zip", 'w')
for path in sub_imgs:
    submission.write(path)
    print('Zip Write '+path)
submission.close()
print('Done.')
