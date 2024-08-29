row = 5

for i in range( 1, row + 1):
    print("* " * i)


'''
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

'''


def count(num):
    
    inc = 0
    
    while num > 0:
        inc = inc + 1
        
        num = num // 10
        
    return inc
        
    
    


num = 23432
x =count(num)
print(x)
