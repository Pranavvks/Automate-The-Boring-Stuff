import os
path=os.getcwd()
for root , dirs , files in os.walk('.'):
    for name in files:
        size=os.path.getsize(path)
        if size > 100000 :
            print(os.path.abspath(name))
    else:
       print("Not found")

