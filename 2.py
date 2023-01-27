#Print even numbers in range 1 to 100 and read the range and print even numbers from the given range
n=int(input())
count=0
for i in range(1,n+1):
    if(i%2==0):
        print(i)
        count=count+1
print(count)
        
