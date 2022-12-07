g_lst=sorted([8,6,7,2])


lst=[0]*(len(g_lst)*2)
print(lst)

idx=0

for i in g_lst:
    lst[idx]=i
    idx +=2

print(lst)
idx=1

for i in range(1,len(lst)+1):
    if i not in lst:
        lst[idx]=i
        idx +=2

print(lst)