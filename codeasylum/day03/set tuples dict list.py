
########################### python data structure #####
 #tuple
v=(1,8,3)
k=(7,8)
#element extract but not change
x=(1,)*4
print(x)
#sets

v=(1,1,2,3)
j={1,3,4,4}
k={3,5}
m={}
print(v)
print(j.intersection(k))
print(len(m))
s=set([1,2,3]) #we can add in it
s.add(5)
print(s)
print(set([1,2]))


#print(v+k)#concatenate of tuple
#list
lst=[1,2,3]
lst[0]=5
print(lst)

#dictionary

mk={'name':'hjain','branch':'cse','college':'nit'}
for i,j in mk.items():
    print(i," ",j)
mk.update(name='Harshit')
print(mk)
p=list(mk[1])
print(p)
ls=[1,2,3]
for i in ls:
    print(i)

    


