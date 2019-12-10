a=(int)(input("enter no"))
rev=0
c=0
k=0
no=a

while a!=0:
    rem=a%10
    
    rev=rev*10+rem
    a=a/10
if no==rev:
    print("palindrome")
else:
    print("not palin")
