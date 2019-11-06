import os

def main():
    name = input("enter username for character file search: ")
    print("searching for " + name)
    readFromFile(name)

def readFromFile(name):
    #get the current file
    currentFile = os.getcwd()
    flag = False
    foundName = ""
    foundFile = ""
    nameArray = []
    #nav back into Data files
    nameFile = open(currentFile + "../../../project2/Data/UserNames.txt", "r")
    if nameFile.mode == "r":
        for names in nameFile:
            nameArray.append(names)
    #searching for names in each file
    for i in range(len(nameArray)):
        #nav back to character files
        file = currentFile + "../../../project2/Characters/" + nameArray[i].strip() + ".txt"
        print("searching file" + file)
        characterFile = open(file, "r")
        for line in characterFile:
            compare = line.split("= ")
            if compare[1].strip() == "John":
                flag = True
                foundName = compare[1].strip()
                foundFile = file

    if flag:
        print("found username: " + foundName + " in file: " +foundFile)
    else:
        print("username was not in any character files")
#to initial the program from __main__
if __name__ == "__main__":
    main()
