import os , shutil
destination= '/home/pranav/Downloads'
for root , dirs , files in os.walk ("."):
    for name in files :
        if name.endswith('.txt'):
            print(os.path.join(root,name))
            source='/home/pranav/'+ str(name)
            dest=shutil.move(source,destination)