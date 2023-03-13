number=int(input("enter number will print all divisors of that number"))
if number<0:
    print("given number is negative please enter positive number")
else:
    i=1;
    while(i*i<number):
        if number%i==0:
            print(i)
        i+=1
    while(i>=1):
        if number%i==0:
            print(number//i)
        i-=1