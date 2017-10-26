import random 

def generator():
    password = ""
    strength = int(input("How strong do you want your password to be? (weak, medium, strong)")) 
    elements= [["apple", "orange", "house", "blues", "horse", "shoe", "integer", "chair", "thermo", "beer"], ["1","2","3","4","5","6","7","8","9","10"],["a","d","g","e","w","q","t","z","h","v"],                  ["!","*", "§", "$", "%", "&", "/","3",">","5"]]
    
    
    if strength == 1:
        number = random.randint(0,9)
        password += elements[0,number]
        print(password)
    
    elif strength == 2:
        mylist= []
        for i in range(4):
            
            number1 = random.randint(0,3)
            mylist.append(numbers[number1])
            number2 = random.randint(0,9)
            mylist.append(elements[number1, number2])
            
            number3 = random.randint(0,9)
            mylist.append(elements[number1, number3])
        
        
        
        
        
        password +="".join(mylist)
        print(password) 
        
        
    #elif strength == "hard":
    
    else:
        print("Your input wasn't correct")
        
generator()