import re
word = " Awesome!  "
regex=re.compile(r'\^s*\s*$')
substiute=re.sub(regex,'',word)
print(substiute)