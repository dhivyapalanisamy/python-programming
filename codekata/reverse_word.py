str=input()
a=str.split(' ')
length=len(a)
for i in range(length):
    temp=a[i]
    reverse=temp[::-1]
    print(reverse,end=' ')
