# arr=[4, 5, 1, 2]
# lst=[]

# for i in range(len(arr)-1,-1,-1):
#     lst.append(arr[i])

# del(arr)

# print(lst)

# lst=lst[::-1]
# print(lst)

arr=[4,5,1,2]
l=0
r=len(arr)-1

while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l +=1
    r -=1

print(arr)