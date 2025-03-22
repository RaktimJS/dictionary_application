import os

def pack(FileName: str):
        dirName = os.path.abspath(FileName)
        dirName = str(dirName)
        dirName = dirName.replace(f"{FileName}", "")

        fileNameWithoutExtension = os.path.splitext(os.path.basename(os.path.abspath(FileName)))[0]

        if os.path.isfile(fileNameWithoutExtension + '.exe') == False:
                os.system(f'pyinstaller --onefile --distpath "." {fileNameWithoutExtension}.py')

        if os.path.exists(dirName):
                os.system(f'rmdir /s /q "{dirName}\\build"')

        if os.path.isfile(fileNameWithoutExtension + '.spec'):
                os.remove(fileNameWithoutExtension + '.spec')
