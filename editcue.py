import os
import shutil
import glob
import re

# 作業対象のパスはカレントに固定している
path = "./"

# 対象のファイル一覧を格納する空リストを新規作成する
target_files=list()

# カレントディレクトリ内のCUEファイル一覧(拡張子を除く)を取得してリストに追加する
for file in glob.glob(path + '*/CDImage.cue'):

    s = str()

    with open(file,'r',encoding='S-JIS') as f:
        for s_line in f:
            if 'FILE' in s_line:
                s = s + 'FILE "CDImage.wav" WAVE\n'
            else:
                s = s + s_line
    
    with open(file,'w',encoding='S-JIS') as f:
        f.write(s)
    
    print(file)

    with open(file,encoding='S-JIS') as f:
        print(f.read())
   




        