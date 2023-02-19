marged_lst=[]

lst1=[1,2,3]
lst2=[1,2]
l1,l2=0,0
#marged_lst=[1,1,2,2,3]
while lst1 or lst2:
    if not lst1:
        marged_lst.append(lst2.pop())
    elif not lst2:
        marged_lst.append(lst1.pop())
    elif lst1[0] >=lst2[0]:
        marged_lst.append(lst2.pop())
    else:
        marged_lst.append(lst1.pop())

print(marged_lst)
