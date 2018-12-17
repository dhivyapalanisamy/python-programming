str=input()
a=len(str)
l=[]
for i in range(a):
    if(str[i]==' ' and str[i+1]==' '):
        continue
    else:
        l.append(str[i])
final=''.join(l)
print(final)
                
