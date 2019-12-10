#factorial
a=(int)(input())
f=1
c=0

for i in range(1,a+1):
    f=f*i
st=str(f)
for i in range(0,len(st)):
    if st[i]=='0':
        c=c+1
print(len(st))
