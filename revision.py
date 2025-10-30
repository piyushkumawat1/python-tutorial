"""marks = {}

x = int(input("Enter your physics marks : "))
marks.update({"phy" : x})
y = int(input("Enter your chemistry mark : "))
marks.update({"Chem" : y})
z = int(input("Enter your math mark : "))
marks.update({"math" : z})

print(marks)"""
'''set = {
    ("int", 9),
    ("float",9.0),
}
print(set)'''
'''values = {
    (9,9.0)
}
print(values)'''

'''count = 1
while count <=10 :
    print(count*count)
    count+=1
'''
'''list = [1,4,9,16,25,36,49,64,81,100]
heroes = ["ironman","thor","hulk","venom","balck panther","spiderman", "doctor strange"]
idx = 0
while idx <= len(heroes)-1 :
    print(heroes[idx],end = "   ")
    idx+=1'''
'''tup = (1,4,9,16,25,36,49,64,81,100)
idx = 0
x = int(input("Give the number :"))
while idx <len(tup) :
    if(tup[idx]) == x:
        print("found at idx",idx)
        break
    else :
        print("finding")   
    idx+=1  '''
'''list = [1,4,9,16,25,36,49,64,81,100,49]
x = 49
idx = 0
for i in list  :
    if(i == x) :
       print("number founded at idx",idx)
       
    idx+=1'''
'''n = int(input("Enter number : "))
for i in range(1,11):
    print(n*i)'''
'''n = int(input("Enter number : "))
i=1 
fact =1
while i<=n :
    fact = fact *i
    i+=1
print("factorial of ",n,"is =",fact)  '''
''''n = int(input("Enter the number : "))
fact = 1
for i in range(1,n+1) :
    fact = fact*i
print("Factorial of",n,"=",fact)    '''
'''n = int(input("Enter the number : "))
sum = 0
while n != 0 :
    reminder = n%10
    sum += reminder
    n = n//10
print("Sum of digits : ",sum)   '''
def cal_sum(a,b):
    sum = a + b
    print("sum of",a,"and",b, "=",sum)
    return sum
cal_sum(34,56)
cal_sum(45,34)
 