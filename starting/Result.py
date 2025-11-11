# Read obtained marks for each subject 
marks = [ ]
for i in range(1,7):
    mark = int(input(f"Enter marks obtained in subject {i}: "))
    marks.append(mark)

# Read maximum marks for each subject
max_marks = [ ]
for i in range(1,7):
    max_mark = int(input(f"Enter maximum marks for subject {i}: "))
    max_marks.append(max_mark)
# Function to calculate total marks and percentage
def calculate(marks,max_marks) :
    total_marks = sum(marks)
    total_max = sum(max_marks)
    percentage = (total_marks/total_max)*100
    return total_marks,percentage
# Function call
total,percent = calculate(marks,max_marks)

#Display results
print(f"\n Total marks obtained :{total}")
print(f"Percentage :{percent:.2f}%")

#Determine division based on percentage 
if percent >= 60 :
   Division = "First Division "
elif percent>=48 :
    Division = "Second Division "
elif percent >=40 :
    division = "Just pass "
else :
    Division = "Failed"
print("Division : ", Division)               

