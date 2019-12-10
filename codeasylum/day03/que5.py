shop={'comb':10,'shoes':3,'pencil':5,'pens':2}
print(list(shop.keys()))
print(list(shop.values()))
lst=[]
for i,j in shop.items():
    lst.append([i,j])
print(lst.sort())

