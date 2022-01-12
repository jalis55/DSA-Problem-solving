lst=[1,2,3,4,5]
x=lst[len(lst)-1]


for i in range(len(lst)-1,0,-1):
    lst[i]=lst[i-1]
    print(lst[i])
lst[0]=x
print(lst)