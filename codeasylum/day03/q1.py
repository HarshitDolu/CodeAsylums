lst=[]
k=0
p=0
s=''
a=(int)(input())
for i in range(a):
    lst.append(input())
for i in range(a):
    s=lst[i]
    p=len(s)
    if len(s)>=2 and s[0]==s[p-1]:
        k=k+1
print(k)
