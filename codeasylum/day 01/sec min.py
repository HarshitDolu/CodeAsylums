lst=[]
sec=0
for i in range(5):
    lst.append((int)(input()))
min=lst[0]
for i in range(5):
    if lst[i]<min:
        first=lst[i]
        sec=min
    if lst[i]<sec and lst[i]!=first:
        sec=lst[i]

print(sec)
