import random 

def generator():
    password = ""
    strength = str(input("How strong do you want your password to be? (weak, strong, very_strong)")) 
    elements= [["apple", "orange", "house", "blues", "horse", "shoe", "integer", "chair", "thermo", "beer"], ["1","2","3","4","5","6","7","8","9","10"],["a","d","g","e","w","q","t","z","h","v"],                  ["!","*", "§", "$", "%", "&", "/","3",">","5"]]
    
    
    if strength == "weak":
        number = random.randint(0,9)
        password += elements[0][number]
        print(password)
    
    elif strength == "strong":
        mylist= []
        for i in range(4):
            
            number1 = random.randint(0,3)
            mylist.append(elements[number1][number1*2])
            number2 = random.randint(0,9)
            mylist.append(elements[number1][number2])
            
            number3 = random.randint(0,9)
            mylist.append(elements[number1][number3])
        
        
        
        
        
        password +="".join(mylist)
        print(password) 
    
    elif strength == "very_strong":
        mylist= []
        for i in range(4):
            
            number1 = random.randint(0,3)
            mylist.append(elements[number1][number1*2])
            number2 = random.randint(0,9)
            mylist.append(elements[number1][number2])
            
            number3 = random.randint(0,9)
            mylist.append(elements[number1][number3])
        
        
        
        
        
        password +="".join(mylist)
        print("Your password is :", password)
        
        
    #elif strength == "hard":
    
    else:
        print("Your input wasn't correct")
        
generator()