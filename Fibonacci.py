def F(n1): 
    if n1<0: 
        print("Incorrect input") 
    
    elif n1==1: 
        return 0
    
    elif n1==2: 
        return 1
    else: 
        return F(n1-1)+F(n1-2) 
    
    F(5)
