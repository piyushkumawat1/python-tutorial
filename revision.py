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
'''def cal_sum(a,b):
    sum = a + b
    print("sum of",a,"+",b, "=",sum)
    return sum
cal_sum(34,56)
cal_sum(45,34)
cal_sum(233223,234234)'''
'''n = int(input("Enter the number : "))
fact = 1
i = 1
while(i<=n):
    fact= fact*i
    i = i+1
print("factorial of",n,"=",fact)   '''

# n = int(input("Enter the number : "))
# reverse = 0
# reminder = 0
# while(n!=0) : 
#     remider = n%10
#     reverse = reverse *10+reminder
#     n =n/10
# print("reverse of numbers =",reverse)    
# list = ["Piyush", 99.99,98,"AI&Ds"]
# list.append("Hello guys")
# list1 = [86.89,23,34,45]
# list1.sort()
# print(" List Sort  = ",list1)
# list1.sort(reverse= True)
# print("List1 sort reverse = ",list1)
# list1.reverse()
# print("List reverse =",list1)
# list1.pop(4)
# print("list pop = ", list1)
# print(list)
# list[0] = "Sakshee"
# print(list)
# list = [1,2,3]
# copy_list = list.copy()
# copy_list.reverse()
# if list == copy_list :
#     print("List is pelendrome ")
# else :
#     print( "List is not pelendromic ")    
# info = {
#     "Name" : input("Enter the name : "),
#     "College" : "PCE",
#     "Branch" : "AI&DS",
#     "Roll_no" : int(input("Enter the roll no :")),
# }
# print("\n")
# print("---->>student information<<----") 
# print("Name of student : ",info["Name"])
# print("College : ", info["College"])
# print("Btanch : ", info["Branch"])
# print("Roll no : ",info["Roll_no"])
