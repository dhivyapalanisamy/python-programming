str=input()
a=len(str)
l=[]
l1=[]
vowel=['a','e','i','o','u']
for i in range(a):
    if str[i] in vowel:
        l.append(str[i])
    else:
        l1.append(str[i])
l3=(l+l1)
final=''.join(l3)
print(final)
              
