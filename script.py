import os
#class to manage the userArray
class Arrhandler:
    def __init__(self):
        self.nameArray = []
    #to get all the user names in an array
    def getAllUserName(self):
        currentFile = os.getcwd()
        nameFile = open(currentFile + "../../../project2/Data/UserNames.txt", "r")
        if nameFile.mode == "r":
            for names in nameFile:
                self.nameArray.append(names.strip())
    #print the array
    def printNameArray(self):
        for i in range(len(self.nameArray)):
            print(self.nameArray[i])

def main():
    #init usernames andfill the array
    allusernames = Arrhandler()
    allusernames.getAllUserName()
    allusernames.printNameArray()

    #file the name in file and if not make a new
    name = input("enter username for character file search: ")
    print("searching for " + name)
    flag = readFromFile(name)

    if not flag:
        gitChangedMakeNewFile(name)
#read the from all chacter files and if the file does not exist or username does
#not exist -> make a new file withname
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

    characterFile.close()
    nameFile.close()
    return flag

def gitChangedMakeNewFile(name):
    print("Change in git status character not found")
    currentFile = os.getcwd()
    #file is not made so make a file and add the Data
    file = open(currentFile + "../../../project2/Characters/" + name +".txt", "w+")
    file.write("username = " + name +"\n")
    #init others to null
    file.write("password = " + "\n")
    file.write("score = " + "\n")
    file.close()

#to initial the program from __main__
if __name__ == "__main__":
    main()
