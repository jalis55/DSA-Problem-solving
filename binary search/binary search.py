def binary_search(nums,key,left,right):
    if left<=right:
        mid=(left+right)//2
        if nums[mid]==key:
            return mid
        else:
            pass


    else:
        return -1



nums=[1,2,3,4,5,6,7,8,9,10,11]
key=8

print(binary_search(nums,key,0,len(nums)-1))

