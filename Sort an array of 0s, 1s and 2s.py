lst=[0,1,2,0,1,2]
m=0
l=0
h=len(lst)-1

while m <= h:
    if lst[m]==0:
        lst[l],lst[m]=lst[m],lst[l]
        l =l+1
        m =m+1
    elif lst[m]==1:
        m =m+1
    else:
        lst[m],lst[h]=lst[h],lst[m]
        h =h-1
print(lst)