# num1 = float(input("Enter the first number : "))
# num2 = float(input("Enter the second number : "))
# sum_result = num1 + num2
# print(f"sum of {num1} + {num2} = {sum_result}")

# SWAPING OF TWO NUMBERS --->
# a = float(input("Enter the number : "))
# b = float(input("Enter the number : "))
# temp = a
# a = b
# b =temp
# print("a  =",a)
# print("b =",b)

#RANDOM NUMBER 
# for i in range(1,11):
#     import random 
#     print(f"Random number : {random.randint(1,100)}")

#CONVERT KILO TO MILES 
# kilometer = float(input("Enter the kilometers : "))

# #convert kilometer to miles (1 km = 0.621 miles)
# conversion_factor = 0.621

# miles = kilometer*conversion_factor

# print(f"{kilometer} is equal to  = {miles}miles")

# CONVERT CELSIUS TO FEHRENIET
# celsius = float(input("Enter the tempareture in celsius : "))

# fehreniet = (celsius *9/2) + 32

# print(f"{celsius}celsius is equal to {fehreniet} fehreniet ")

#SOLVE A QUADRATIC EQUATION = aX^2 + bX +c
# import math
# a= float(input("Enter the cofficient a : "))
# b= float(input("Enter the cofficient b : "))
# c= float(input("Enter the cofficient c :"))

# discrimant = b**2 -4*a*c
# if discrimant >0 :
#     Root1 = -b + math.sqrt(discrimant) / 2*a
#     Root2 = -b + math.sqrt(discrimant) / 2*a
#     print(f"Root1 : {Root1}")
#     print(f"Root2 : {Root2} ")
# elif discrimant ==0 :
#     Root = -b/2*a 
#     print(f"Root : {Root}") 
# else :
#     Real_part = -b /2*a
#     imaginary_part = math.sqrt(abs(discrimant))/2*a   
#     print(f"Root1 = {Real_part} + {imaginary_part}i") 
#     print(f"Root2 = {Real_part} - {imaginary_part}i")  

#SWAPING THE NUMBER WITHOUT USING THIRD VARIABLE
# a = float(input("Enter the number : "))
# b = float(input("Enter the number : "))
# print(f"Before swaping a = {a} and b ={b}")
# a,b =b,a
# print(f"After the swaping a ={a} and b= {b}")

#FIND THE NUMBER(POSITIVE ,NEGATIVE ,ZERO)
# num = int(input("Enter the number : "))
# if num >0 :
#     print(f"{num} is positive number ")
# elif num <0 :
#     print(f"{num} is negative number ")
# else :
#     print(" number is zero")     

#FIND THE NUMBER IS ODD AND EVEN
# num = int(input("enter the number : "))
# if num%2 ==0 :
#     print("Number is even")
# else :
#     print("Number is odd")   

# FIND THE YEAR IS LEAP OR NOT 
# year = int(input("Enter the year : "))

# if ((year%4==0 and year!=100) or (year%400 == 0 and year%100 ==0)) :
#     print(f"{year} is a leap year")
# else :
#     print(f"{year} is not leap year ")    

# FIND THE PRIME NUMBER 
# num = int(input("Enter the number : "))
# if num%2 ==0 :
#     print(f"{num} is a prime number ")
# else :
#     print(f"{num}is not a prime number ")    

#FIND THE PRIME NUMBER BETWEEN 1 TO 10
# num =int(input("Enter the number : "))
# for i in range(1,num) :
#     if(i%2==0) :
#         continue
#     else :
#         print(i)

#FIND THE FACTORIAL OF NUMBER 
# factorial =1
# num = int(input("Enter the number : "))
# for i in range(1,num+1):
#     factorial =factorial*i

# print(f"Factorial of {num} = {factorial}") 

# PRINT THE TABLE OF NUMBER         
# num =int(input("enter the number of table : "))
# for i in range (1,11) :
#     print(f"{num}x{1} = {num*i}")

#ARMSTRONG NUMBER 
# num = int(input("Enter the number : "))
# num_str = str(num)
# sum = 0
# sum_power =len(num_str)
# temp =num
# while temp>0 :
#     reminder = temp%10
#     sum = sum + reminder ** sum_power
#     temp//=10
# if sum == num :
#     print(f"{num} is armstrong number ")
# else :
#     print(f"{num} is not armstrong number ")


#num = int(input("Enter the number : "))
# num_str = str(num)
# sum = 0
# sum_power =len(num_str)
# temp =num
# while temp>0 :
#     reminder = temp%10
#     sum = sum + reminder ** sum_power
#     temp//=10
# if sum == num :
#     print(f"{num} is armstrong number ")
# else :
#     print(f"{num} is not armstrong number ")

# FIND ARMSTRONG NUMBER IN INTERVEL
# num = int(input("Enter the number interval(1-n) : "))
# for i in range (1,num+1):        
#     num_str = str(i)
#     sum = 0
#     sum_power = len(num_str)
#     temp = i
#     while temp>0 :
#        reminder = temp%10
#        sum = sum + reminder ** sum_power
#        temp//=10
#     if sum == i :
#        print(f"{i} is armstrong number ")


        
# SUM OF N NATURAL NUMBER 
# Num = int(input("Enter the number : "))
# sum = 0
# for i in range (1,Num+1) :
#     sum+=i
# print(f"Sum of n natural number :{sum}")    
    
   
#calculate fabonacci 
# def fab_num(num) :
#      if(num ==1): 
#         return 1
#      elif(num ==0) :
#         return 0
#      else :
        
#         return fab_num(num-1) + fab_num(num-2)
# num = int(input("Enter the number : "))     
# print(f"fabonacci of {num} = {fab_num(num-1) + fab_num(num-2)}")

# fab_num(num)  
