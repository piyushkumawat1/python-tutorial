# import random
# # Take a random number 
# target = random.randint(1,10) 
# while True :
#  num = (input("Enter the number or for quit(Q) : "))
#  if num.upper() == "Q" : 
#    break
#  num = int(num)
#  print("Random number  = ",target)
#  if num == target :
#     print("Number is match ")
#     print("Congratualation -- correct guess ")
#     break
#  elif(num>target) :
#    print("Your number is greater than random number ")

#  elif(num <target) :
#    print("your number is less than random number ")  

# print("----GAME OVER----")   

# Password generate ----->>>
import random 
import string
pass_len = 4
charValues= string.digits #+ string.ascii_letters + string.punctuation
# method-1 

#(list comprehension[function for i in range(n)])

#Password = "".join([random.choice(charValues) for i in range(pass_len)])
#method - 2

Password = ""
for i in range (pass_len):
   Password+=random.choice(charValues)
print("Your random password = ",Password) 
Try = 0
for i in range (3) :
 password = input("Enter the password : ")
 if password == Password :
   print("System unlocked ")
   break
 else :
   print("Wrong password") 
   print("Try again") 
   Try+=1
   if Try ==3:
     print("Your tries are finished")
     print("Your system is locked")
 