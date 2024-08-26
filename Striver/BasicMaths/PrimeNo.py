# Prime No 

def prime(N):
    
    count = 0
    
    for i in range(1 , N + 1):
        
        if N % i == 0:
            
            count = count + 1
            
    if count == 2:
        
        True
    else:
        False
            



def prime2(N):
    
    
    # intlize c value
    c = 0
   
   
   # i intlize a iteration and then increment a N + 1 (1, N + 1) is increment 
    for i in range(1, N + 1):
        
        # Mdole the number and used a for loops 
        if N % i == 0:
            
            # increment
            c = c + 1
        
        # chek N is 
        if N == 2:
            return True
        
        else:
            return False
       


if __name__ == "__main__":
    
    
    N = 5
    
    isPrime = prime2(N)
    
    if isPrime:
        
        print(N, "Prime")
    
    else:
        
        print(N, "Not Prime")
    

 
 
 
 