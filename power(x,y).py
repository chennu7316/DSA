x=int (input("we are finding pow(x,y) please enter x here"))
y=int(input("please enter y here"))
def power(x,y):
    res=1;
    while y>0:
        if y&1:
            res=res*x
        x*=x
        y=y>>1
    return res

print(power(x,y))
