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
tup = (1,4,9,16,25,36,49,64,81,100)
idx = 0
x = int(input("Give the number :"))
while idx <len(tup) :
    if(tup[idx]) == x:
        print("found at idx",idx)
        break
    else :
        print("finding")   
    idx+=1     