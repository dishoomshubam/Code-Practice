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

def pattern3(n):
    
    
 for i in range(n, 0, -1):
    print("* " * i)
      



pattern3(n)