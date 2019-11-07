import os
#class to manage the userArray
class UsersHandler:
    def __init__(self):
        self.name_array = []
        self.current_file = os.getcwd()
        self.user_file_path = self.current_file + "../../../project2/Data/UserNames.txt"
    #to get all the user names in an array
    def get_all_user_names(self):
        name_file = open(self.user_file_path, "r")
        if name_file.mode == "r":
            for names in name_file:
                self.name_array.append(names.strip())
        name_file.close()
    #print the array
    def print_name_array(self):
        for i in range(len(self.name_array)):
            print(self.name_array[i])
    #add a new user to the file
    def add_new_user(self, name):
        name_file = open(self.user_file_path, "a+")
        file.write(name)
        file.close()
    #save all the user names
    def save_file(self):
        self.sort_file()
        name_file = open(self.user_file_path, "w+")
        for i in range(len(self.name_array)):
            name_file.write(name_array[i])
        name_file.close()
    #just to sort array
    def sort_file(self):
        self.name_array.sort()

#manages file Reading
class CharacterHandler:
    def __init__(self, name):
        self.name = name
        self.current_file = os.getcwd()
        self.character_file_path = self.current_file + "../../../project2/Data/UserNames.txt"
        #read the from all chacter files and if the file does not exist or username does
        #not exist -> make a new file withname
    def search_for_name(self):
        print("searching for name in character directory")
        flag = False
        found_name = ""
        found_file = ""
        name_array = []
        #nav back into Data files
        name_file = open(self.character_file_path, "r")
        if name_file.mode == "r":
            for names in name_file:
                name_array.append(names)
        #searching for names in each file
        for i in range(len(name_array)):
            #nav back to character files
            file = self.current_file + "../../../project2/Characters/" + name_array[i].strip() + ".txt"
            print("searching file" + file)
            character_file = open(file, "r")
            for line in character_file:
                compare = line.split("= ")
                if compare[1].strip().lower() == self.name.lower():
                    flag = True
                    found_name = compare[1].strip()
                    found_file = file

            if flag:
                print("found username: " + found_name + " in file: " +found_file)
            else:
                print("username was not in any character files")

            character_file.close()
            name_file.close()
            return flag
        #makes a new character file
    def git_changed_make_new_file(self):
        print("Change in git status character not found")
        #file is not made so make a file and add the Data
        file = open(self.current_file + "../../../project2/Characters/" + self.name +".txt", "w+")
        file.write("username = " + self.name +"\n")
        #init others to null
        file.write("password = " + "\n")
        file.write("score = " + "\n")
        file.close()


def main():
    #init usernames andfill the array
    all_user_names = UsersHandler()
    all_user_names.get_all_user_names()
    strs = input("print all active users (y/n)?: ").lower()
    #only check yes otherwise assume no
    if(strs[0] == "y"):
        all_user_names.print_name_array()


    #file the name in file and if not make a new
    name = input("enter username for character file search: ")
    #make a character object from the name
    character_name = CharacterHandler(name)
    flag = character_name.search_for_name()
    if not flag:
        #make a new character file and add user name to user name file
        character_name.git_changed_make_new_file()
        all_user_names.add_new_user(name)

#to initial the program from __main__
if __name__ == "__main__":
    main()
