n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
y=[] 
c=0
for i in l:
    if i not in y:
        y.append(i)
    else:
        c+=1
print(l)
print('count=',c)
