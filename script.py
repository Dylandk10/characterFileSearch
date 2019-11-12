import os
import sys
from datetime import date
from datetime import datetime
from sys import platform
#class to manage the userArray
class UsersHandler:
    def __init__(self):
        self.name_array = []
        OS_file_path = OSFileHandler()
        self.user_file_path = OS_file_path.get_username_file_path()
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

class CharacterHandler:
    def __init__(self, name):
        self.name = name
        OS_file_path = OSFileHandler()
        self.username_file_path = OS_file_path.get_username_file_path()
        self.character_file_path = OS_file_path.get_character_file_path()
        self.metadata_file_path = OS_file_path.get_metadata_file_path()
    #search all characters and see if the character exist
    def search_for_name(self):
        print("searching for name in character directory")
        flag = False
        found_name = ""
        found_file = ""
        name_array = []
        #nav back into Data files
        name_file = open(self.username_file_path, "r")
        if name_file.mode == "r":
            for names in name_file:
                name_array.append(names)
        #searching for names in each file
        for i in range(len(name_array)):
            #nav back to character files
            file = self.character_file_path + name_array[i].strip() + ".txt"
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
        file = open(self.character_file_path + self.name +".txt", "w+")
        file.write("username = " + self.name +"\n")
        #init others to null
        file.write("password = " + "\n")
        file.write("score = " + "\n")
        file.close()
    #update the character file
    def update_character_file(self, password, score):
        print("Change in git status character not found")
        #file is not made so make a file and add the Data
        file = open(self.character_file_path + self.name +".txt", "w+")
        file.write("username = " + self.name +"\n")
        #init others to null
        file.write("password = " + password + "\n")
        file.write("score = " + score + "\n")
        file.close()
    #make a meta data file
    def make_meta_data_file(self):
        today = date.today()
        str1 = today.strftime("%m/%d/%y")
        timestamp = datetime.now()
        str2 = str(timestamp.hour) + ":" + str(timestamp.minute) + ":" + str(timestamp.second) + ":" + str(timestamp.microsecond)
        meta_file = open(self.metadata_file_path + self.name +".txt", "w+")
        meta_file.write(str1 + "\n")
        meta_file.write(str2)
        meta_file.close()

#class to handle the paths for each file
#made easier to use with mac/linux and windows
class OSFileHandler:
    def __init__(self):
        self.path = ""
    #handle UserName file paths
    def get_username_file_path(self):
        if platform == "win32":
            self.path = os.getcwd() + "../../../project2/Data/UserNames.txt"
        else:
            self.path = "../../project2/Data/UserNames.txt"
        return self.path
    #handles getting thr character file path
    def get_character_file_path(self):
        if platform == "win32":
            self.path = os.getcwd() + "../../../project2/Characters/"
        else:
            self.path = "../../project2/Characters/"
        return self.path
    #return the meta data file math
    def get_metadata_file_path(self):
        if platform == "win32":
            self.path = os.getcwd() + "../../../project2/Meta/"
        else:
            self.path = "../../project2/Meta/"
        return self.path

#controls the menu and sub menus
class InputHandler:
    def __init__(self):
        self.input = ""
        self.all_user_names = UsersHandler()
    #main menu for script
    def main_menu(self):
        self.input = input("Update character or search for character: ").lower()
        if self.input == "update" or self.input[0] == 'u':
            self.update_menu()
        elif self.input == "search" or self.input[0] == 's':
            self.search_menu()
        elif self.input == "exit" or self.input == "quit" or self.input[0] == 'e' or self.input[0] == 'q':
            sys.exit()
        else:
            print("invalid command")
            self.main_menu()
    #the menu for updating character properties
    def update_menu(self):
        #file the name in file and if not make a new
        name = input("enter username for character file search: ")
        #make a character object from the name
        character_name = CharacterHandler(name)
        flag = character_name.search_for_name()
        if not flag:
            #make a new character file and add user name to user name file
            character_name.git_changed_make_new_file()
            all_user_names.add_new_user(name)
    #menu to search for character
    def search_menu(self):
        strs = input("Search for character name or print all names: ")
        if strs == "search" or strs[0] == 's':
            self.search_characters()
        elif strs == "print" or strs[0] == 'p':
            self.print_all_characters()
        else:
            print("command not found")
            self.search_menu()
    #sub menu to search for character
    def search_characters(self):
        strs = input("Enter the name to search for: ")
        character_name = CharacterHandler(strs)
        flag = character_name.search_for_name()
        if flag:
            print("found user name " + strs)
        else:
            print("user name not found check files")
        self.main_menu()
    #method to print all the character
    def print_all_characters(self):
        self.all_user_names.get_all_user_names()
        self.all_user_names.print_name_array()
        self.main_menu()

#starts the program
def main():
    #inits the main menu
    menu = InputHandler()
    menu.main_menu()


#to initial the program from __main__
if __name__ == "__main__":
    main()
