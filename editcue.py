import os
import shutil
import glob
import re

# 作業対象のパスはカレントに固定している
path = "./"

# 対象のファイル一覧を格納する空リストを新規作成する
target_files=list()

# 錆ディレクトリ内のCUEファイルを対象にする
for file in glob.glob(path + '*/CDImage.cue'):

    # 空の文字列を入れる箱を用意する
    s = str()

    # Shift-JISでCUEファイルを開く
    with open(file,'r',encoding='S-JIS') as f:
        # 1行毎にCUEファイルを読み込む
        for s_line in f:
            # 行にFILEが含まれている場合はCDImage.wavに置き換えるて箱に追加する
            if 'FILE' in s_line:
                s = s + 'FILE "CDImage.wav" WAVE\n'
            # それ以外の場合はそのまま箱に追加する
            else:
                s = s + s_line
    
    # CUEファイルを書き込みモードで開き、箱の内容で上書きする。
    with open(file,'w',encoding='S-JIS') as f:
        f.write(s)
    
    # 変更結果を出力する。
    print(file)
    with open(file,encoding='S-JIS') as f:
        print(f.read())
           