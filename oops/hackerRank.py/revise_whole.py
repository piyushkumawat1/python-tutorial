# str = input("Enter the name : ")
# len = len(str) 
# print("Length of name:",len)
# print(str.count("$"))
# print(str[0:len])
# print(str.endswith("i"))
# print(str.capitalize())
# print(str.replace("piyush","Saksheee"))
# print(str.count("p")) #count the occurancce of substring

age = int(input("Enter the age : "))
light = input("Enter the single : ")
if age <18 or light == "red ":
    print("Your not eligible for vode and drive")
elif (age>18 or light == "red"): 
    print("You are eligible to vote and drive")    