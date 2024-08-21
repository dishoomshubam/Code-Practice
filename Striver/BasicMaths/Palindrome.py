# for loops


# def Palindrome3(z):
    
#     if z < 0:
#         return False
#     if z >= 0 and z <= 10:
#         return True
    
#     dec = 0
#     ori = z
    
#     while z > 0:
#         dec = dec * 10 + z & 10
        
#     return ori == dec
    
    


# z = 123
# l = Palindrome3(z)
# print(l)

# def palindrome(n):
#     dec = 0
#     digit = str(n)
    
#     for num in digit[::-1]:
#         id = int(num)
        
#         dec = (dec * 10) + id
         
#     if dec == n:
        
#         print("palindrome")
#     else:
#         print("not Palindrome")
        
#     return dec
    
    
    


# n = 5515 
# out = palindrome(n)
# print(out)

# while

# def palindrome1(num):
#     dec = 0
    
#     while num > 0:
        
#         id = num % 10
        
#         dec = (dec * 10) + id
        
#         num = num // 10
        
#     if num == id:
#         print("palindrome Num")
#     else:
#         print("not palindrome")
        
        
#     return dec
    
    
# num = int(input())
# num2 = palindrome1(num)
# print(num2)


# def Palindrome2(x):
#     dec = 0
#     string = str(x)
    
#     for number in string[::-1]:
#         id = int(number)
        
#         dec = (dec * 10) + id
        
        
        
#     return dec
    
    
# x = 12
# put = Palindrome2(x)
# print(put)





def practice(x):
    rever_num = 0
    orignal = str(x)
    
    for number in orignal[::-1]:
        add = int(number)
        
        rever_num = rever_num * 10 + add
        
    if rever_num == orignal:
        True 
    else:
        False
        
    return rever_num == x
    


x =int(input()) 
z = practice(x)
print(z)


    