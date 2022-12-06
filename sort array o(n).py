lst=[7,8,1,2,5,4]
l,r=0,1
ar=[]
while True:
    if r==len(lst):
        ar.append(lst[l])
        lst.remove(lst[l])
        
        l,r=0,1
    if len(lst)==1:
        ar.append(lst[0])

        break
    if lst[l]>lst[r]:
        l=r
    r +=1
print(ar)