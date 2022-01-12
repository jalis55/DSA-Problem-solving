arr=[4, 5, 1, 2]
lst=[]

for i in range(len(arr)-1,-1,-1):
    lst.append(arr[i])

del(arr)

print(lst)

lst=lst[::-1]
print(lst)