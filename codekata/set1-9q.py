n=int(input("enter size of array"))
k=int(input("enter k elements to add"))
m=0
l=[]
for i in range(0,n):
    t=int(input())
    l.append(t)
for i in range(0,k):
    m=m+l[i]
print(m)
    
