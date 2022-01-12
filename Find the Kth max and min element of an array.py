arr =[7,10,4,3,20,15]
K = 4
min=0
#sorting

for i in range(len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
        if arr[min_idx]>arr[j]:
            min_idx=j
            
    arr[i],arr[min_idx]=arr[min_idx],arr[i]
        

print(f"{K}th element is {arr[K-1]}")