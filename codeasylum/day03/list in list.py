lst=[1,4,5,[2,3,9],8,[5,7],9]
n=[]
h=[]
b=len(lst)
for i in range(b):
    if type(lst[i])==type(n):
        p=0
        
        k=len(lst[i])
        p=lst[i]
      
        
        for j in range(k):
            print(" ",p[j])
    else:
        print(lst[i])

