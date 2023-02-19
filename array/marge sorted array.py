marged_lst=[]

lst1=[1,2,3]
lst2=[1,2,5]


while lst1 or lst2:
    if not lst1:
        marged_lst.append(lst2.pop(0))
    elif not lst2:
        marged_lst.append(lst1.pop(0))
    elif lst1[0] >=lst2[0]:
        marged_lst.append(lst2.pop(0))
    else:
        marged_lst.append(lst1.pop(0))

print(marged_lst)
