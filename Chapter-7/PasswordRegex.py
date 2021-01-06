import re
def strongPassword(password):
    if Regexsearch1.search(password)==None:
        return False
    if Regexsearch2.search(password)==None:
        return False
    if Regexsearch3.search(password)==None:
        return False
   if Regexsearch4.search(password)==None:
        return False


Regexsearch1=re.compile{8 , } 
Regexsearch2=re.compile{r'\d+'}
Regexsearch3=re.compile{[A-Z]+}
Regexsearch4=re.compile{[a-z]+}

if strongPassword("Thisiscool8") == True :
    print("Strong password")
else:
    print("Wrong Password")