#python program to find factorial of a number
n=int(input())
fact=1
if n<0:
    print("does not exist")
elif n>=0:
    for i in range(2,n+1):
        fact=fact*i
print(fact)
