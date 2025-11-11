# class Student :
#     college_name = "Poornima college"

#     def __init__(self,name,marks,branch):
#         self.name = name
#         self.marks = marks
#         self.branch = branch

# s1 = Student("Piyush kumawat",97,"AI&DS")
# s2 = Student("Sakshee kumawat",99,"ARTS")
# print(f"Name ={s1.name}\n",f"marks = {s1.marks}\n",f"Branch ={s1.branch}")
# print(f"Name ={s2.name}\n",f"marks = {s2.marks}\n",f"Branch ={s2.branch}")
        
    
# class Student :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def Average_marks(self) :
#         sum = 0
#         for val in self.marks :
#             sum+=val
#         self.marks = sum/3
#         print(f"hi {self.name} your average score = {self.marks} ")     
# S1 = Student("Piyush",[97,98,99])
# S1.Average_marks()              

# class Car :

#     def __init__(self,mode):
#         self.mode = mode
#         self.acc = False
#         self.brk = False
#         self.cultch = False
        

#     def start(self) :
#         self.acc = True
#         self.brk = True
#         self.cultch = True
#     print("car started ....")    
# car1 =Car("start")  
# print(car1.mode)  
   

# class Account :
#     def __init__(self,balance,acc):
#         self.balance = balance
#         self.account_no = acc

#     #debit mathod
#     def debit(self,amount) :
#         self.balance-=amount
#         print("Rs",amount,"was debited ")
#         print("Final balance = ",self.get_balance())
        

#     #debit method
#     def credit(self,amount):
#         self.balance+=amount
#         print("Rs",amount,"was credited")
#         print("Final balance = ",self.get_balance())
        
#     def get_balance(self):
#         return self.balance
                 
# acc1 = Account(10000,98875)
# print("Account no = ",acc1.account_no)
# acc1.credit(1000)


    