# class Account :
#     def __init__(self,acc,balance):
#         self.account_no = acc
#         self.balance = balance
#     @staticmethod 
#     def greeting() :
#          print("Welcome to HDFC BANK OF INDIA ")   

#     def credit (self,amount) :
#           self.balance += amount
#           print(f"Rs{amount} was credited  ")
#           print(f"Final balance  = {self.get_balance()}") 

#     def debit (self,amount) :
#          self.balance-=amount
#          print(f"Rs{amount} was debited ")
#          print(f"Final balance = {self.get_balance()}")   

#     def get_balance(self):
#          return self.balance
# Account.greeting()
# cust1= Account(6372,10000)
# print("Account no :",cust1.account_no) 
# cust1.credit(1000)   
# cust1.debit(3453)         
       
    







class Account :
    def __init__(self,acc,balance):
        self.acc = acc
        self.balance = balance
    @staticmethod
    def welcome():
        print("Welcome to HDFC bank ")


    def credit(self,amount) :
        self.balance+= amount
        print(f"{amount} was credited")

    def debit(self,amount) :
        self.balance-=amount
        print(f"{amount} was debited")  

    def get_balance(self):
        return self.balance
    
        
cus1 = Account(6372,10000)
cus1.welcome()
cus1.credit(1000)
cus1.debit(2354)

print("Final balance :",cus1.get_balance())


class Order :
    def __init__(self,item ,price):
        self.item = item
        self.price = price

    def __gt__(self,ord2) :
        return self.price > ord2.price



ord1 = Order("Tea",10)
ord2 = Order("samosa",25)


print(ord1.price<ord2.price)


     