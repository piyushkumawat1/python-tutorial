with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using java.\nI like programmingin java.")
word = "learning"
with open("practice.txt","r") as f :
     data = f.read()
     Update_data = data.replace("java","python")    
def check_for_word ():
    with open("practice.txt","w") as f:
     f.write(Update_data)
    if Update_data.find(word) !=  -1 :
            print("Found")
    else :
            print("Not found") 
def check_for_line ():
    word = "learning" 
    line_no = 1
    data = True                
    with open("practice.txt","r") as f :
       while data : 
            data = f.readline()
            if (word in data ) :   
               print(line_no)
               return 
            line_no+=1
       return -1
    
check_for_line()    
            
         
