import os , re
from pathlib import Path
p=Path('/home/pranav/Downloads')
files=list(p.glob('*.pdf'))
for filer in files:
    heading=open(filer ,'rb')
    reader=heading.read()
    print(list (reader.decode('latin-1')))

    for i in heading :
        regex=re.compile('Can\'t|English|Automate')
        mo=regex.search(regex)
