def gcd(n1, n2):
    
    gcd = 1
    
    for i in range(1, min(n1, n2) + 1):
        
        if n1 % i == 0 and n2 % i == 0:
            
            gcd = i
            
    return gcd
    


n1 = 12
n2 = 6

call = gcd(n2 , n1)
print(call)





def find_the_gcd(h1,h2):
    
    # intnlize a gcd = 1 because 1 is all num are divided 
    
    gcdh = 1
    
    
    # for loop to chek both num h1 and h2
    for i in range(1, min(h1, h2) + 1):
        
        # chek the codition both are divided or not both are divided then show a one similer num other wise show a 1
        if h1 % i == 0 and h2 % i == 0:
            
            gcdh = i
            
            
    return gcdh
            
    
    

h1, h2 = 11, 21

call = find_the_gcd(h1, h2)
print(call)