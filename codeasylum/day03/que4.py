dict1={'1':1,'2':2,'3':3,'4':1}
lst=[]
print(dict1.values())
for i,j in dict1.items():
    if j not in lst:
        lst.append(j)
print(lst)
