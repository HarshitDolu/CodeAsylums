#Addrev
def rev(a):
    rem=0
    rev=0
    while a!=0:
        rem=a%10
        rev=rev*10+rem
        a=a/10
    return rev

a=(int)(input())
b=(int)(input())
a1=rev(a)
a2=rev(b)
a3=a1+a2
k=rev(a3)
print(k)
