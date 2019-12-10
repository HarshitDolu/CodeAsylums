
str="HeLlo"
s=""
for i in range(len(str)):
    if ord(str[i])>=65 and ord(str[i])<=90:
        k=ord(str[i])+32
        s=s+chr(k)
    else:
        k=ord(str[i])-32
        s=s+chr(k)
print(s)
