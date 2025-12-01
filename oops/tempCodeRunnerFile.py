# class Student :
#    college = "Poornima college of engineering"
#    def __init__(self,name,branch,roll_no) :
#       self.name = name
#       self.branch = branch
#       self.roll_no = roll_no
# i = 1
# while i <=10 :
#    name  = input("Enter the student's name : ")
#    branch = input("Enter the student's branch :")
#    roll_no = int(input("Enter the roll no : "))
#    s = Student(name,branch,roll_no)
#    print("Student's college :",s.college)
#    print("Student's name ",s.name)
#    print("Students branch",s.branch)
#    print("Student's roll no : ",s.roll_no)
# #    print("\n")


# #    i = i+1
# class Student :
#     def __init__(self,name,phy,chem,math) :
#         self.name = name
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @staticmethod
#     def hello() :
#         print("hello")     


# s1 = Student("Piyush kumawat",89,87,98)
# s2 = Student("Raj Singh",99,98,100)
# print("Student's name : ",s1.name)
# print("Physics marks : ",s1.phy)
# print("Chemistry marks : ",s1.chem)
# print("Math marks : ",s1.math) 
# avg = round( (s1.phy + s1.chem + s1.math  )/ 3)
# print("Average  = ",avg)     

# print("\n")
# print("Student's name : ",s2.name)
# print("Physics marks : ",s2.phy)
# print("Chemistry marks : ",s2.chem)


class Account :
    def __init__(self,acc,bal) :
        self.account = acc
        self.balance = bal

    def credit(self,amount) :
        self.balance = self.balance + amount
        print(f"{amount} was credited on your account")

        
    def debit(self,amount) :
        self.balance = self.balance - amount
        print(f"{amount} was debited from account")
        
acc1= Account(432412,10000) 
acc1.credit(1000)
acc1.debit(2331)
print("Account no.  : ",acc1.account)
print("Final amount : ",acc1.balance)