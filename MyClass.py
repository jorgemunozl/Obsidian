import os
import subprocess
class Menu(Note): #each time we call menu, we ask for a input?
    def  __init__(self):
        print("1. Create a new note")
        print("2. View Notes(Only view, not modify)")
        print("3. Modify a notes")
        print("4. Exit")
    def choose(self):
        option=int(input("Option: "))
        return option
    def createNewNote(self):
        opt_0=input("Do you want specify the path?(y/n)")
        opt_1=input("Do you want use a Template?(y/n)")
        if opt_0=='y':
            os.chdir(path_root)
                         
        name=input("Enter the name of the note:")
        path=self.path
        if name.exist():
            print("Exist a note with this name!!")
            opt=(input("Do you specify another name (s) or visualize the note (v)?(s/v)"))
            if opt=="s":
                name=input("Enter the name of the note:")
                note=Note(name,path)

            else:
                
    def viewNote(self):
class Obsidian():
    def __init__(self,path):
        self.name=name
        self.path=path
    def run(self)
        menu=Menu()
        opt=menu.choose()
        if (opt==1):
            vault.createNewNote()
        elif(opt==2):
            vault.()
        elif (opt==3):
            vault.modify()
            else: 
        vault.out()
        print("SAYONARA")
    def view_note(self):
        pass
    def modify(self):
        print("modifying")
    def out(self):
        #modify the flag
        flag=False

class search():
    def __init__(self,name,path):
        #name=
        #take it to lowercase
        self.name=name
        self.path=path
    def bus():
        location=os.listdir(path)
        print("📂📂📂FOLDERS📂📂📂")
        for archivo in location:
            if not archivo.endswith(".md") and "." not in archivo:
                print(" --- ",(archivo))
        print("📁📁📁FILES MD📁📁📁")
        for archivo in location:
            if archivo.endswith(".md"):
                print(" - ",(archivo))
        search=input("SEARCHING : ")

        print("🔍🔍🔍SEARCHING🔍🔍🔍")
        for archivo in location:
            #retire the .md for better
            #implement letter search
            if search in archivo.lower() and "." in archivo:
                print(archivo)
class Note(Obsidian): 
    def __init__(self,name,path_note): #We know name and path's note
        self.name=name
        self.path_note=path_note
    def noteadd(self):
        os.chdir(self.path_note)
        subprocess.call(["nano",name])            
        print("Note created")
    def delete(self):
        os.chdir(self.path_note)
        os.remove(name)
    def visualize(self):
        with open(name,"r") as f:
            content=f.read()
            print(content)
class Template(Note):


