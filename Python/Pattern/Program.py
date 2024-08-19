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
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i - 1))
    
    # Bottom part of the diamond
      for i in range(n, 0, -1):
        # Print leading spaces
        print(' ' * (n - i), end='')
        # Print stars
        print('*' * (2 * i - 1))
 
#  '''
#    *
#  ***
# *****
# *****
#  ***
#   *
# '''
  
def p9(n):
    # First part: Increasing pattern
    for i in range(1, n + 1):
        print("*" * i)
        
        # Second part: Decreasing pattern
    for j in range(n -1, 0, -1):
        print("*" * j)
        
def num(n):
    for inc in range(1, n + 1):
        print("1" * inc)

# num(n)     
# p9(n)




def oe(n):
    for i in range(1, n + 1):
        
        start_num = 1 if i & 2 != 0 else 0
        
        
        row= []
        
        for j in range(i):
            row.append(str(start_num))
            
            start_num = 1 - start_num
            
            
        print(" ".join(row))
        
# oe(n)


def odeven(n):
    for inc in range(1, n + 1):
        
        num = 1 if inc % 2 != 0 else 0
        
        data = []
        
        for dec in range(inc):
            
            data.append(str(num))
            
            num = 1 - num
            
        print(" ".join(data))
  
# odeven(n)



def num(n):
    for i in range(1, n + 1):
        num = 1 if i % 2 != 0 else 0
        
        data = []
        
        for j in range(i):
            data.append(str(num))
            
            num  = 1 -num
            
            
        print(" ".join(data))


# num(n)
'''

0
1 0
1 0 1


'''

def mir(n):
    
   for i in range(1, n + 1):
       
       First = [str(j) for j in range(1, i + 1)]
       
       Mirror = [str(j) for j in range(i, 0, -1)]
       
       
       spaces = " " * (2 * (n - i))
       
       print(" ".join(First) + spaces + " ".join(Mirror))
        
        
# mir(n)




def Mirror(n):
    for i in range(1, n + 1):
        
        Left = [str(j) for j in range(i, n + 1)]
        Right = [str(j) for j in range(i, 0, -1)]
        
        
        spaces= " " * ( 2 * ( n -i))
        
        print( " ".join(Left) + spaces + " ".join(Right))
        
        
# Mirror(n)

'''

1    1
1 2  2 1
1 2 33 2 1

'''


def numTri(n):
    counter = 1
    
    for i in range(1, n + 1):
        row = []
        
        for j in range(i):
            row.append(str(counter))
            
            counter += 1
            
        print(" ".join(row))
        
# numTri(n)


def Numtr(n):
    count = 1
    
    for i in range(1, n + 1):
        
        data = []
        
        for j in range(i):
            data.append(str(count))
            
            count += 1
            
            
        print(" ". join(data))


# Numtr(n)
'''
1
2 3
4 5 6

'''

def chat(n):
    for i in range(1, n + 1):
        
        data = [ char(65 + j) for j in range(i)]
        
        
        print(" ".join(data))

# chat(n)




def alpha(n):
    for i in range( 1, n + 1):
       
        data = [chr(65 + j) for j in range(i)]
            
        print(" ".join(data))
    
    
    
# alpha(n) 




def alphab(n): 
    
    for inc in range(1, n + 1):
        
        data = [chr(65 + j) for j in range(inc)]
        
        print(" ".join(data))

# alphab(n)



'''
A
A B
A B C

'''



def alpapluse(n):
    
    for i in range(1, n + 1):
        
        letter = chr(65 + ( i - 1))
        
        data = " ".join([letter] * i)
        
        print(data)


def alpaprac(n):
    for i in range(1, n + 1):
        
        letter = chr(65 + (i - 1))
        
        data = " ".join([letter] * i)
        
        print(data)   

# alpaprac(n)
# alpapluse(n)


def letter(n):
    
    for increment in range(1, n + 1):
        
        letter = chr(65 + (increment - 1))
        
        data = " ".join([letter] * increment)
        
        print(data)

letter(n)

'''
A
BB
CCC
'''


#  question completed a around 15-16