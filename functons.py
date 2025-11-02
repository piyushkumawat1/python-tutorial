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
def show(n) :
    if(n==100):
      return 0
    print(n)
    show(n+1) 

show(int(input("Enter the number : ")))      