def listString(n):
    string=","
    return(string.join(n))
spam=['apples' , 'bananas' , 'tofu', 'cats']
spam[2]="and"
print(listString(spam))