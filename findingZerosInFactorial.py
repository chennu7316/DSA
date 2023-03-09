number=int(input("enter a number which we need to find number of zeros in given facorial"))
i=5;
sum=0;
while i<=number:
    sum+=number//i;
    i=i*5;
print("Number of zeros present in given  facorial number is ",sum)
