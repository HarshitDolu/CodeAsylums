#lst=[]
#print("enter the size of list:")
#n=(int)(input("enter the size"))
#for i in range(n):
 #   lst.append((int)(input()))
#for i in range(n):
    #   if lst[i]>0:
     #   print(lst[i]*lst[i]*lst[i])
    #else:
     #   print(lst[i],end="")
      #  print("is a negative number")
 

a=(int)(input("enter no"))
rev=0
c=0
k=0
while a>0:
    rem=a%10
    c=c+1
    rev=rev*10+rem
    a=a/10

while c!=0:
    k=0
    re=(int)(rev%10)
    for i in range(re):
        print("hello",end=" ")
        k=k+1
        print(k,end=" ")
        
    rev=rev/10
    c=c-1
    

