str=input()
a=len(str)
l=[]
for i in range(a):
    if(str[i]==' '):
        continue
    else:
        l.append(str[i])
final=''.join(l)
print(final)
