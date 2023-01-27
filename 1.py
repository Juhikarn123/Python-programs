# Program to check if a number is prime or not

n=int(input())
count=0
if n==1:
    print("not a prime")
elif n>1:
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if(count==2):
        print("prime")

    else:
        print("not prime")


