from MyClass import Obsidian


path="/home/vault/'Second Brain'"

vault=Obsidian("Second Brain",path)

flag=vault.flag
while(flag):
    vault.options()
    option=vault.input_user()
    if (option==1):
        vault.create_note()
    elif(option==2):
        vault.view_note()
    elif (option==3):
        vault.modify()
    else: 
        vault.out()
        print("SAYONARA")