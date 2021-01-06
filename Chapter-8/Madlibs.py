import re

file=open('madlibs.txt')
text=file.read()
file.close()

regex=re.compile(r'(NOUN) | (ADJECTIVE) | (VERB)')

for i in regex.findall(text):
            reg=re.compile(r'{}'.format(i))
            Input=input('Enter the substitute for noun,adjective or verb  ' )
            text=reg.sub(Input,text,1)
print(text)
file=open('madlibschange.txt','w')
file.write(text)
file.close()
