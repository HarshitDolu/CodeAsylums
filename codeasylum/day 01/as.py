a=(int)(input("enter the no:"))
r=a%6
if r==0 or r==1:
    print("window seat")
if r==2 or r==5:
    print("middle seat")
if r==3 or r==4:
    print("side seat")
k=a+6
print(k)
