def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    return a//b
    
def remainder(a,b):
    return a%b
    
print("--Simple Calculator--")
print("Operations:-")
print("1. Addition") 
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
operation=int(input("Enter the operation to perform [1/2/3/4/5]:"))

num1=float(input("Enter the 1st number: "))
num2=float(input("Enter the 2nd number: "))

if operation==1:   
    print(f"The sum of {num1} and {num2} is",addition(num1,num2))

elif operation==2:   
    print(f"The difference between {num1} and {num2} is",subtraction(num1,num2))

elif operation==3:   
    print(f"The product of {num1} and {num2} is",multiplication(num1,num2))

elif operation==4:  
    if num2==0:
        print("Error: Division by zero is not possible")
    else:
        print(f"The quotient of {num1} and {num2} is",division(num1,num2), "and their remainder is",remainder(num1,num2))

elif operation==5:
    print("Thank you for using the calculator")

else:
    print("Invalid operation!!! Try again.")