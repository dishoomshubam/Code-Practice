def count(n):
       # Initialize a counter variable
    countNum = 0
    
        # While loop iterates until 'n'
    while n > 0:
          # Increment the counter
        countNum = countNum + 1
         # Divide 'n' by 10 to
        # remove the last digit.
        n = n // 10
          # Return the
    # count of digits.
    return countNum


if __name__ == "__main__":
    n = 1231111111
    digit = count(n)
    print(digit)


# 
# Brute Force Approach
    # 
import math


def countDigits(n):
    
    count = 0
    
    while n > 0:
        count = count + 1
        
        n = n//10
        
    return(count)
    
    


n = 234567
co = countDigits(n)
print(co)


# Optimal Approach


def Optimal(num):
    
    # math fun integrated and then + 1
    
    count = (int(math.log10(num) + 1))
    
    # return a count
    
    return count

    
num = int(input())
    
Approach = Optimal(num)

print(Approach)



####################

def Evenly( n):
  a = 0
  
  while n > 0:
      
      a = a + 1
      
      n = n // 10
      
  return a


n = 4124
Odd = Evenly(n)
print(Odd)