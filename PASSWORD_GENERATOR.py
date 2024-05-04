print("--WELCOME TO THE PASSWORD GENERATOR--")
length=int(input("Enter the length of the password you want to generate:- "))
uppercase=input("Do you want to include uppercase letters? (y/n) ")
lowercase=input("Do you want to include lowercase letters? (y/n) ")
digits=input("Do you want to include digits? (y/n) ")
char=input("Do you want to include special characters? (y/n) ")

password=''
if uppercase=="y":
    