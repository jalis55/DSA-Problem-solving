lst=[1,3,5,2,4,1]
sorted_lst=[]

while lst !=[]:
    m=min(lst)

    sorted_lst.append(m)
    lst.remove(m)

print(sorted_lst)
