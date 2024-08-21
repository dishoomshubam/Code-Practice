def revers(n):
    
    reverNum = 0
    
    while n > 0:
        
        id = n % 10
        
        reverNum = (reverNum * 10) + id
        
        n = n // 10
        
    return reverNum
        
        
    
n =12
num = revers(n)
print(num)







def revised(n):
    
    dec = 0
    
    while n > 0:
        
        id = n % 10
        
        dec = (dec * 10) + id
        
        n = n // 10
        
    return dec
    
    


n = 123123
out = revised(n)
print(out)



#  For Loops 

def revisedFor(n):
    
    dec = 0
    
    string = str(n)
    
    for digit in string[::-1]:
        id = int(digit)
        
        dec = (dec * 10) + id
        
    return dec
 
    
    
n = 1231231
out = revisedFor(n)
print(out)