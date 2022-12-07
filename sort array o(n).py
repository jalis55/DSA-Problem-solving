lst=[7,8,1,2,5,4]
l,r=0,1
ar=[]
length=len(lst)
while True:
    if r==length:
        ar.append(lst[l])
        lst.remove(lst[l])
        l,r=0,1
        length -=1
    if length==1:
        ar.append(lst[0])
        break
    if lst[l]>lst[r]:
        l=r
    r +=1
print(ar)