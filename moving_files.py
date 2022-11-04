import os
import shutil

fromdir = "C:/Users/user/Downloads"
todir = "C:/Users/user/Desktop/"

listOfFiles = os.listdir(fromdir)

for fileName in listOfFiles:
    name, nameExtension = os.path.splitext(fileName)

    if nameExtension == " " :
        continue

    if nameExtension == ['.jpg', '.jpeg', '.png', '.jfif', '.pdf', '.txt', '.txtas']:
        path1 = fromdir + "/" + fileName
        path2 = todir + "/" + "'Documents'"
        path3 = todir + "/" + "'Documents'" + "/" + fileName

        print("from:", path1)
        print("to:", path3)

        if os.path.exists(path2):
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)