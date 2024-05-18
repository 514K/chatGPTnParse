import os

lstFiles = []
def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        else:
            if it.path.find("-new.txt") != -1:
                lstFiles.append(it.path)

listdirs("./textready_final")

for i in lstFiles:

    fileName = str(i).replace("-new", "")
    print(i)
    print(fileName)
    with open(i, "r", encoding="utf-8") as f:
        txt = f.read()[1:-1]
        f.close()

        with open(fileName, "w", encoding="utf-8") as f2:
            f2.write(txt)
            f2.close()

    os.remove(i)