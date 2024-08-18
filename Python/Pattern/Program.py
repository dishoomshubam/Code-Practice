n = 3

def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
            
        print()
    


def pattern1(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
            
        print()
'''
1
22
333
4444
55555
'''

def pattern4(n):
 for i in range(n, 0, -1):
    print("* " * i)

'''
* * * 
* * 
* 
'''


def p5(n):
    for i in range(n, 0,  -1):
        for j in range(1,i + 1):
             print( j,end=" ")
        print()

'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

def p6(n):
    for i in range(n):
        print(" "*(n - i - 1), end="")
        print("*" * (2 * i + 1))
    

'''
 *
 ***
*****
'''

def p7(n):
    for i in range(n):
        
        print(" " * i, end="")
        print("*" *(2 * (n - i) - 1))

'''
*****
 ***
  *
  '''

def p8(n):
    for i in range(1, n + 1):
        print(" "*(n - i - 1), end="")
        print("*" * (2 * i + 1))
    for i in range(n, 0, -1):
        print(" " * i, end="")
        print("*" *(2 * (n - i) - 1))
        
 
    
p8(n)