while True:
    print("Enter your age: ") # Here the condition is set to be true ,
    age=input()
    if age.isdecimal():
        break
    print("Please enter a no for your age.") #Check the indentation here print will not be printed definitely as it is a block of code within the while loop. Hence when break statement is encounterd the program terminates.
while True:
    print("Select a new password(letters and numbers only):")
    password=input()
    if password.isalnum():
        break
    print("Password is awesome")