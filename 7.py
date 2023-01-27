#Print the product of even numbers and odd numbers 
n=int(input())
ep=1
op=1
for i in range(1,n+1):
    if(i%2==0):
        ep=ep*i
    elif(i%2!=0):
        op=op*i
print("ep is",ep)
print("op is",op)
    
