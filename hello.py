# Calculator for two numbers 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
# Arithmetics operations 
Addition = a+b
Substraction = a-b
Multiplication = a*b 
Division = a/b
Modulas = a%b 
# User input for operation
type  = (input( "Enter a character :"))
if type == '+':
    print("Addition of two number is :", Addition)
elif type =='-':
    print( "Substraction is :", Substraction)
elif type =='*':
    print("Multiplication of two number is :", Multiplication )
elif type == '/':
    print('Division of two numbers is : ', Division)
elif type == '%':
    print("Modulas of two number is : ", Modulas)
else:
    print("Invalid operator")                