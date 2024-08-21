def Armstrong(num):
    
    length = len(str(num))
    # print(length)
    
    sum = 0
    
    n = num
    
    while n > 0:
        
        id = n % 10
        
        sum += id ** length
        
        n = n // 10
        
    return sum == num






def main():
    num = 153
    if Armstrong(num):
        print(num, "is palinfor")
    else:
        print(num, "not pal")
    
if __name__ == "__main__":
    main()



    


# for loops

def ArmstrongFor(number):
    
    str_num = str(number)
    leng_num = len(str_num)
    
    sum = 0
    
    for digit in str_num:
        sum += int(digit) ** leng_num
        
    return sum == number
        


def main():
        
    number = 153
    if ArmstrongFor(number):
        print(number, "Armstrome")
    else:
        print(number, "Not Armstrome")
        
if __name__ == "__main__":
        main()
        
