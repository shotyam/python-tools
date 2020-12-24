import os
import shutil

path = "./"
target_files=list()

for file in os.listdir(path):
    base, ext = os.path.splitext(file)
    if ext == '.cue':
        target_files.append(base)

for item in target_files:
    new_path = path + item
    os.mkdir(new_path)

    # CUEファイル
    target_cue = path + item + '.cue'
    new_cue = new_path + '/CDImage.cue'
    print(target_cue)
    print(new_cue)

    shutil.move(target_cue, new_cue)

    # WAVファイル
    target_wav = path + item + '.wav'
    new_wav = new_path + '/CDImage.wav'
    print(target_wav)
    print(new_wav)

    shutil.move(target_wav, new_wav)






    



