a=[2,2,1,2,2,5,5,6]
lst=[]
for i in a:
    if i not in lst:
        lst.append(i)
print(lst)
