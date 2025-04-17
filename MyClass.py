import os



class Obsidian():
    flag=True
    #atributes? use of @ I dunno know
    def __init__(self,name,path):
        self.name=name
        self.path=path
        print("Welcome to Obsidian")
        print("Do you like this terminal version?")
        print("Of course, you can use the GUI version, but this is how it works")
    def options(self):
        print("1. Create a new note")
        print("2. View Notes(Only view, not modify)")
        print("3. Modify a notes")
        print("4. Exit")
    def input_user(self):
        option=int(input("Option: "))
        return option
    def create_note(self):
        name=input("Enter the name of the note:")
        print("Created note, now you write the content")
        content=input("Content: ")
        print("Note created")
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

class Note():
    pass

