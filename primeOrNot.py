number =int(input("enter number for checking prime number"));


def primeOrNot(num):
    if(num==1):
        return False
    elif num%2==0 or num%3==0:
        return False
    else:
        i=5;
        while(i*i<=num):
            if num%i==0 or num%(i+2)==0:
                return False
            i+=6;
    return True

if(number<0):
    print("enter positive number")
else:
    if primeOrNot(number):
        print("given number is prime") 
    else:
        print(" given number is not a prime number")
    