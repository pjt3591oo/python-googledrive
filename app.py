from utils.google_drive import download, upload

import os


if __name__ == '__main__':
    file_name = 'test.xlsx'
    file_save_dir = './result/google_drive_download/'

    f = os.path.join(file_save_dir, file_name)
    download.down('1Ko-qeL8zCk4AxKmT00Nw2pO_0uFRZ7d2OH_UhIXqxzM', f)  # 다운로드 파일

    f = os.path.join(file_save_dir, 'somefile.txt')  # 업로드 파일
    upload.up(f)