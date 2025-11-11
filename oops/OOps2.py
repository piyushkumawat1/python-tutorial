#using ""del"" keyword to delete our object 
# class Student :
#     def __init__(self,name,place):
#         self.name = name
#         self.place = place

# s1 = Student("Raj","Rajsthan")  
# print(s1.name,"\n",s1.place)
# del s1
# print(s1)
# class Person :
#     __name1 = "Raj singh "
#     __name2 = "Vijay kumawat"
#     def __init__(self) :
#         pass
#     @staticmethod
#     def welcome():
#         print("Hello Student  ")
#         print("--* Personal information*--")

#     def __hello(self) :
#         print("Hello !")

#     def Raj_details(self,age):
#         self.__hello()
#         print("Name =",self.__name1) 
#         print("age =",age)
#     def Vijay_details(self,age) :
#         self.__hello()
#         print("Name =",self.__name2)
#         print("age =",age)

# per = Person()
# per.welcome()
# per.Raj_details(17) 
# per.Vijay_details(18)     

#learn about inheritance       
# class car :
#     @staticmethod
#     def start():
#         print("Car started...")
#     @staticmethod
#     def stop() :
#         print("Car stopped...")
            
# class Toyota(car):
#     def __init__(self,name):
#         self.name = name
#         print(self.name)

# car1 =Toyota("Fortuner")
# car1.start()
# print("Arrived the destination")
# car1.stop()
# print("\n")
# car2 = Toyota("Innova")
# car1.start()
# print("Arrived the destination")
# car1.stop()  


# class A :
#     varA= ("Welcome to class A") 

# class B :
#     varB =("Welcom to class B")
# class C(A,B):
#     varC = ("welcome to class C")
# class1 = C()  
# print(class1.varA)           
        

# class Car :
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car stopped...")

# class Toyota(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type) # super()method which is used to access the method of parents class

# car1 =Toyota("Fortuner","electric")
# print(car1.name)
# print(car1.type)

#class method use 
# class Person:
#     name = "Anonymous"
#     #def __init__(self,name):
#      #   Person.name = name
#     @classmethod
#     def changeName(cls,name):
#         cls.name = name

# p1= Person()
# p1.changeName("Rahul kumawat")
# print(p1.name)
# print(Person.name)   


# use of {property} decoder to update the parameter which we through in obj atrributs
# class Student:
#     def __init__(self ,phy ,math,chem) :   
#         self.phy = phy
#         self.math = math
#         self.chem = chem
#         percentage = str((self.phy +self.chem +self.chem) /3)
#     @property
#     def percentage(self):
#         return str((self.phy +self.chem +self.chem) // 3)+"%"
    

# stu1 = Student(98,97,99)
# print("physics marks =",stu1.phy)
# print("Chemistry marks =",stu1.chem)
# print("Math marks =",stu1.math)
# print("Percentage =",stu1.percentage)
# stu1.phy = 100   
# print("There have issue to check number in physics. recheckng... ") 
# print("after the update ")

# print("physics marks =",stu1.phy)
# print("Chemistry marks =",stu1.chem)
# print("Math marks =",stu1.math)
# print("Percentage =",stu1.percentage)
#print("Sorry for this mistake ")

# class Complex :
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img
#     def shownumber(self) :
#         print(self.real,"i +",self.img,"j")

#     def __add__(self,num2):
#         Newreal =self.real + num2.real
#         Newimg = self.img + num2.img
#         return Complex(Newreal , Newimg)
#     def __sub__(self,num2):
#         Newreal =self.real - num2.real
#         Newimg = self.img -  num2.img
#         return Complex(Newreal , Newimg)
    
#     def __mul__(self,num2) :
#         Newreal =self.real * num2.real - self.img * num2.img
#         Newimg = self.img * num2.img + self.img *  num2.real
#         return Complex(Newreal , Newimg)
# num1 =Complex(3 , 4)
# num2 = Complex(4,6)
# num1.shownumber()
# num2.shownumber()
# num3 = num1 *  num2 
# num3.shownumber()
# QUESTIONS
# class Circle :
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14*self.radius**2
#     def perimeter(self):
#         return 2*3.14*self.radius


# cir =Circle(21)

# print("Area of circle : ",cir.area())
# print("Perimeter of circle :",cir.perimeter())

# class Employee :
#     def __init__(self,role,department,salary) :
#         self.role = role
#         self.department = department
#         self.salary = salary

#     def showDetails(self) :
#         print("Role = ",self.role)
#         print("department= ",self.department)
#         print("Salary = ",self.salary) 
# Emp1= Employee("Softweer Engineer","software",1000000)
# Emp1.showDetails()     

# class Enginner (Employee):
#     def __init__(self,age ,name):
#         self.age = age
#         self.name = name
#     def showDetails(self):
#         print("Name =",self.name)
#         print("age = ",self.age)
#         super().__init__("Softweer Engineer","software",1000000)    

# eng = Enginner(21,"Piyush kumawat")
# eng.showDetails()

class Order :
    def __init__(self,item,price):
        self.item = item
        self.price= price

    def __gt__(self,ord2):
        return self.price>ord2.price    

ord1= Order("Chips" ,20)
ord2 = Order("Samosa",15)

print(ord1.price<ord2.price)

