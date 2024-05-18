import os, sys, openai

openai.api_key = sys.argv[1]

lstFiles = []
def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            listdirs(it)
        else:
            if it.path.find(".txt") != -1 and it.path.find("-new.txt") == -1:
                lstFiles.append(it.path)
            
prompt = ""
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.readline()

rootdir = sys.argv[2]
listdirs(rootdir)
count = 0
for item in lstFiles:
    with open(item, "r", encoding="utf-8") as f:
        count = count + 1
        text = f.read()
        oldtext = text
        f.close()

        textLst = []
        while len(text) > 4000:
            textLst.append(text[:4000])
            text = text[4000:]
        
        textLst.append(text)
 
        newText = ""
        for itemText in textLst:
            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "user", "content": prompt + "\n" + itemText + ""}
              ]
            )

            newText = newText + completion.choices[0].message.content

        with open(item[:-4] + "-new.txt", "w", encoding="utf-8") as f2:
            print("[\nold:\n{};\nnew:\n{}\n]".format(oldtext, newText))
            f2.write(newText)
            f2.close()

