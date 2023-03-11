num1=int(input("enter num1"))
num2=int(input("enter num2"))
def gcd(a,b):
    if b==0:
        return a;
    return gcd(b,a%b)
res=gcd(num1,num2)

def lcm(num1,num2):
    return num1*num2//gcd(num1,num2)
print("GCD OF TWO NUMBERS",res)
print("LCM OF TWO NUMBERS",lcm(num1,num2))