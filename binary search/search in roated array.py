def search(nums,target,l,r):
    if l<=r:
        mid=(l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>=nums[l]:
            if nums[mid]>=target and nums[l]<=target:
                return search(nums,target,l,mid-1)
            else:
                return search(nums,target,mid+1,r)
        else:
            if target>=nums[mid] and nums[mid]<=nums[r]:
                return search(nums,target,mid+1,r)
            else:
                return search(nums,target,l,mid-1)
    else:
        return -1



nums=[4,5,6,1,2,3]
target=2

print(search(nums,target,0,len(nums)-1))