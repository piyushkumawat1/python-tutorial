marks = {}

x = int(input("Enter your physics marks : "))
marks.update({"phy" : x})
y = int(input("Enter your chemistry mark : "))
marks.update({"Chem" : y})
z = int(input("Enter your math mark : "))
marks.update({"math" : z})

print(marks)