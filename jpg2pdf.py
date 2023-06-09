import img2pdf
import os
import re
import shutil
from PIL import Image
from pathlib import Path
def main():
    print('画像を結合したい対象ディレクトリを入力してください')
    img_Folder = input('>> ')
    if(img_Folder[-1:]!="\\"):
        img_Folder=img_Folder + '\\'
    folder_name=img_Folder.split('\\')[-2]
    base_Image = img_Folder
    path = Path(base_Image)
    Create_pdf=path.parent
    images = sorted([str(p) for p in path.glob('**/*') if re.search('/*\.(jpg|jpeg|png)', str(p), re.IGNORECASE)])
    folder_name_pdf=folder_name+'.pdf'
    path_pdf_name = os.path.join(Create_pdf, folder_name_pdf)
    if os.path.exists(path_pdf_name): 
        while True:
            answer = input("上書きしますか？ (はい/いいえ)")
            if answer == "はい":
                with open(path_pdf_name, "w") as f:
                    f.write(img2pdf.convert(images))
                break
            elif answer == "いいえ":
                break
    with open(path_pdf_name , "wb") as f:
        f.write(img2pdf.convert(images))
if __name__ == "__main__":
    main()