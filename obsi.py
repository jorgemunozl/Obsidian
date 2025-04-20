from MyClass import Obsidian

path="/home/vault/'Second Brain'"

vault=Obsidian(path)

vault.run()


flag=vault.flag
while(flag):
    vault.options()
    option=vault.input_user()
    