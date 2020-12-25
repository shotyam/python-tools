import os
import shutil

# 作業対象のパスはカレントに固定している
path = "./"

# 対象のファイル一覧を格納する空リストを新規作成する
target_files=list()

# カレントディレクトリ内のCUEファイル一覧(拡張子を除く)を取得してリストに追加する
for file in os.listdir(path):
    base, ext = os.path.splitext(file)
    if ext == '.cue':
        target_files.append(base)

# リスト内の作業対象に対して各操作を行う
for item in target_files:

    # ディレクトリの新規作成
    new_path = path + item
    os.mkdir(new_path)
    print('フォルダ作成:' + new_path)

    # CUEファイルの移動
    target_cue = path + item + '.cue'
    new_cue = new_path + '/CDImage.cue'
    shutil.move(target_cue, new_cue)
    print('ファイル移動:' + target_cue + '->' + new_cue)

    # WAVファイルの移動
    target_wav = path + item + '.wav'
    new_wav = new_path + '/CDImage.wav'
    shutil.move(target_wav, new_wav)
    print('ファイル移動:' + target_wav + '->' + new_wav)






    



