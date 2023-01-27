#Print sum of even numbers and odd numbers 
n=int(input())
esum=0
osum=0
for i in range(1,n+1):
    if(i%2==0):
        esum=esum+i
    elif(i%2!=0):
        osum=osum+i
print("esum is",esum)
print("osum is",osum)
    
