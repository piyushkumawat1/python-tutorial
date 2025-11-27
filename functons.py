'''def cal_product(a,b) :
    sum = a*b
    print(sum)
    return a*b
cal_product(1,3)'''
'''heroes = ["ironman", "thor ","shaktiman", "captain ameriaca","spiderman","dr strange"]
def len_list(list) : 
    for item in (list): 
       print(item , end =", ")
len_list(heroes)'''
'''def cal_fact(n):
    fact=1
    for i in range(1,n+1) :
        fact = fact*i

    print(f"Factorial of {n} =",fact)
cal_fact(int(input("Enter the number : "))) '''
'''def conv_currency(doller) :
    rupees = doller* 89 
    print(f"{doller} USD = ",rupees,"INR")
conv_currency(int(input("Enter the  amount of doller : ")))    '''
'''def check(num) :
    if num %2 ==0:
        print("Even ")
    else :
        print("odd number")  
check(int(input("Enter the numebr : ")))   '''
'''def show(n) :
    if(n==100):
      return 0
    print(n)
    show(n+1) 

show(int(input("Enter the number : ")))      '''
'''n =int(input("Enter the number  :"))
def fact(n) :
    if(n ==0 or n==1) :
        return 1
    else :
        return n*fact(n-1)
    

fact(n)
print("Facrtorial of",n,"=",n*fact(n-1))'''
'''n = int(input("Enter the number : "))
sum = 0
def cal_sum(n) :
    if(n==0) :
        return 0
    return cal_sum(n-1) +n
    
sum = cal_sum(n)
print("Sum  = ",sum)'''

'''list = ["Ironman", "Superman", "thor", "black panther"]
def print_list(list, idx) :
    if(idx == len(list)) :
        return 
    print(list[idx])
    print_list(list,idx +1 )  

print_list(list,0)'''
'''n = int(input("Enter the number : "))
def cal_sum(n) :
    if(n==0):
        return 0
    else :
        return cal_sum(n-1) +n
    
sum = cal_sum(n)
print("Sum = ",sum)    '''
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()
# def print_table(num) :
#   while num<=100 :
#     print(num)
#     num +=1
# num  = int(input("Enter the number : "))    
 

# list = []
# n = int(input("Enter the number : "))
# while n <=10 :
#     sqrt = n*n
#     list.append(sqrt)
#     n +=1
# print(list)  
  
x = int(input("Enter the number : "))
list = []
for j in range (10,20) :
        list.append(j)
i = 1
while i <= 10 :
    if x == list[i] :
        print(f"Number {list[i]} is found at {i} index")
        break
    else :
        print("Finding....") 
    i +=1           
   