# class Student :
#     def __init__(self,name,marks) :
#         self.name = name
#         self.marks = marks

#     def get_avg(self) :
#         sum = 0 
#         for val in self.marks :
#             sum +=val  

#         print("hi",self.name,"your average score is",sum/3)


# s1 = Student("Piyush kumawat",[98,99,97])
# s1.get_avg()          
# class Car :
#     def __init__(self) :   # Constructor 
#         self.acc  = False
#         self.brk = False 
#         self.clutch = False


#     def Start(self) :

#         self.acc = True
#         self.clutch = True
#         self.brk = False
#         print("Car started ...")

# Car1 = Car()

# Car1.Start()
# class Account :
#     def __init__(self, acc ,bal) :
#         self.acc = acc 
#         self.bal = bal
    

#     def credit(self,amount) :
#       self.bal+=amount
#       print("Final amount : ",self.bal)
#       return self.bal
    
#     def debit(self,amount): 
#        self.bal -= amount
#        print("Final amount : ",self.bal)
#        return self.bal


# cus1= Account(1234,10000)
# cus1.credit(500)
# cus1.debit(100)
# class Account :
#     def __init__(self,Acc_no,Acc_pass) :
#         self.account_no = Acc_no 
#         self.__account_pass = Acc_pass

# account_pass  = int(input("Enetr the password : "))
# c1 = Account(1234,account_pass) 
# print('Account Number :',c1.account_no) 
# class Person : 
#     def __init__(self,name) :
#         self.name = name


#     def __hello(self) :
#         print(f"Hi {self.name} buddy ")
#     def welcome(self) :
#         self.__hello() 
# s1 = Person("Piyush")
# s1.welcome()
# class Car :
#     def __init__(self,type) :
#         self.type = type
#         self.start  = False
#         self.brk =False
#         self.clutch = False
#     def str(self) :
#         self.start = True
#         self.brk = True
#         self.clutch = True
#         print("Car started... ")

# class Toyotacar(Car) :

#     def __init__(self,brand,color,type) :
#         self.brand = brand
#         self.color = color
#         self.type = type
#     def car_start(self) :
#         self.start = True
#         self.brk = False
#         self.clutch = True
#         super().__init__(type)
#         print(f"{self.brand} started...")
# car1 = Toyotacar("Fortuner","Black","electric")
# print(car1.brand)
# print(car1.color)
# print(car1.type)
# car1.car_start()      

# class Person : 
#     name  = "Anonymous"
#     def changName(self,name) :
#         self.name =name 
        

# p1 = Person()
# print(p1.changName("rahul"))        
# class Person : 
#     name = "Anonymous"
#     # def changename(self,name) :
#     #     self.name = name 
#     @classmethod
#     def changename(obj,name) :
#         obj.name = name


# p1 = Person()  
# p1.changename("Rahul shaab")    
# print(Person.name)
# print(p1.name)
# class Student :
#     def __init__(self,phy,chem,math) :
#         self.math = math
#         self.chem = chem
#         self.phy = phy
#         #self.percentage = str((self.chem +self.phy + self.math)/3)+"%" 

#     @property
#     def percentage(self) :
#             return str((self.chem +self.phy + self.math)/3)+"%" 



# s1  = Student(97,98,99) 
# print(s1.percentage)
# s1.phy = 34
# print(s1.percentage)
        
# class Student :
#     name = "Anonymous"
#     @classmethod
#     def Changename(self,name) :
#         self.name = name 

# s1 = Student()
# s1.Changename("Piyush kumawat")
# print(s1.name)
# print(Student.name)


# class Complex :
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNum(self) :
#         print(self.real,"i","+",self.img,"j")

#     def __add__(self,num2) :
#         newreal = self.real + num2.real    
#         newimg = self.img + num2.img
#         return Complex(newreal,newimg)


# num1 = Complex(1,3)
# num1.showNum()  
# num2 = Complex(2,4)
# num2.showNum()  
# num3 = num1 + num2 
# num3.showNum()     

# class Circle : 
#     def __init__(self,radius) :
#         self.radius = radius


#     def area(self) :
#         return 3.14 *self.radius**2 

#     def perimeter(self) :
#         return 3.14*2*self.radius  

# n = float(input("Enter the radius of circle : "))  

# c1 = Circle(n)
# print("Area of circle : ",c1.area())
# print("perimeter of circle",c1.perimeter())  
# class Employee :
#     def __init__(self,dep,role,salary) :
#         self.dep = dep 
#         self.role = role
#         self.salary = salary

#     def showDetails(self) :
#         print("role :",self.role)
#         print("department:",self.dep)
#         print("salary :",self.salary)
# Emp1 = Employee("Software","cloud engineer",100000)


# class Engineer(Employee) :
#     def __init__(self,name,age) :
#         self.name = name
#         self.age = age
#         super().__init__("Software","cloud engineer",100000)
#     def showDetails(self) :
#         print("Name :",self.name)
#         print("age : ",self.age)
#         super().showDetails()
# Emp = Engineer("Piyush kumawat",21)
# Emp.showDetails()
# import random
# target = random.randint(1,100)
# while True :
#     userChoice = input("Enter the Choice or Quit(Q) :")
#     if userChoice=='Q' :
#         break
#     userChoice = int(userChoice)
#     if userChoice == target : 
#         print("Congrats you guess correct")
#         print("-------GAME OVER------") 
#     elif userChoice > target :
#         print("Your number was to big please choose small number  ")
#     else :
#         print("your choice was too small guess big one ")

# import random 
# import string 
# pass_len = 4
# password = ""
# values = string.ascii_letters + string.digits + string.punctuation
# for i in range(pass_len) :
#     password += random.choice(values)
# print(password)











# import random
# import string
# pasa_len = 6
# values = string.ascii_letters + string.digits + string.punctuation
# password = ""
# for i in range(pasa_len) :
#   password += random.choice(values)
# print(password)
# def Try(count = 1) :
#     pass_lock = input("Enter the password  :")
#     if password == pass_lock : 
#      print("Device Unlocked ")
#     else : 
#       print("Wrong password Please Try again ")
#       if count == 3 : 
#         return 
#       else : 
#         Try(count+1) 
        
# Try()        
        

import random

choices = ["rock" ,"paper", "sessor"]

while True : 
     computer  = random.choice(choices)
     userchoice = input("Choose (rock ,paper,sessor or quit) : ").lower()
     print("Computer choice ",computer)
     if userchoice == "quit" : 
       print("GAME OVER ")
       break
     elif computer == userchoice : 
         print("Tie ")
     elif userchoice not in choices :
         print("Invalid choice")     
     elif ((computer == "rock" and userchoice == 'sessor') \
           or (computer == "paper" and userchoice == "rock") \
            or computer == 'sessor' and userchoice == "paper" ) :
         print("You lose")
     else : 
         print("You win")   
 
  
