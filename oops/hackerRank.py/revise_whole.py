# str = input("Enter the name : ")
# len = len(str) 
# print("Length of name:",len)
# print(str.count("$"))
# print(str[0:len])
# print(str.endswith("i"))
# print(str.capitalize())
# print(str.replace("piyush","Saksheee"))
# print(str.count("p")) #count the occurancce of substring

# age = int(input("Enter the age : "))
# light = input("Enter the single : ")
# if age <18 or light == "red ":
#     print("Your not eligible for vode and drive")
# elif (age>18 or light == "red"): 
#     print("You are eligible to vote and drive")    


# def factorial(n) :
#     fact = 1 
#     for i in range(1,n+1) :
#       fact *= i
#     print(f"Factorial of {i} =", fact)

# def convert(usd_val) :
#    ind_val = 89*usd_val
#    print(f"{usd_val:.2f} USD = {ind_val:.2f} INR")
# DOller = float(input("Enter the Doller : "))   
# convert(DOller)   
# num  = int(input("Enter the number : "))
# def find_num(num) :
#     if num %2 == 0 :
#         print("Even number ")
#     else :
#         print("Odd number ")
# find_num(num)
# def fact(n) :
#     if (n == 0 or n ==1 ) :
#         return 1
#     else :
#         return n * fact(n-1)
# n  = int(input("Enter the number : "))    
# s = fact(n)      
# print(f"Factorial of {n} = {s}")
# def cal_sum(n) :
#     if n == 0 :
#         return 0
#     return  cal_sum(n-1) + n
# sum = cal_sum(10)
# print("Sum = ",sum)
# lst = [1,2,3,4,"kumar"]        
# def print_list(lst,idx) :
#     if idx > len(lst) - 1 :
#         return 
#     print(f"At {idx} index = {lst[idx]} ")
#     print_list(lst,idx+1)

# print_list(lst,0)  
# def check_for_word(word) :
#      with open("sample.txt","r") as f :
#        data = f.read()
       
#      with open("sample.txt","r") :
#       if data.find(word) != -1 :
#          print("Found")
#       else :
#          print("Not found")  

# def check_for_line() :
#    word = "learning"
#    line_no = 1
#    with open("sample.txt","r") as f :
#       data = True
#       while data :
#         data = f.readline()
#         if word in data :
#            print(line_no)
#         line_no+=1   
# check_for_line()       
            
with open("sample.txt","r") as f :
    data = f.read()
    list = data.split(",")
    count = 0
    for val in list :
        if (int(val) %2 == 0 ) :
            count+=1
    print("Total Even number =",count)           