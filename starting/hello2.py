# make a calculator for two numbers 
num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
# operator which take a input from user and operation between to operands 
operator = input("Enter the operator : ")
if operator == '+':
    addition = num1 + num2
    print(addition)
elif operator == '-':
    if num1>num2 : 
       substraction = num1 - num2
    else :
        substraction = num2 - num1
    print(substraction)
elif operator == '*' : 
    multiplication = num1*num2 
    print(multiplication)   
elif operator == '/' :
    division = num1/num2
    print(division)             