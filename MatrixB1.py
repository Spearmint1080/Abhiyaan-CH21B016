m,n=map(int,input().split()) #Obtaining size of Matrix
k=int(input())  #obtaining Target
s="false"  #Default
for i in range(m):
    a=list(map(int,input().split())) #Obtaining each row
    for j in range(n):
        if(a[j]==k): #Checking if target exists
            s=f"true\n{i} {j}"  #Storing Target Index
print(s)

            
