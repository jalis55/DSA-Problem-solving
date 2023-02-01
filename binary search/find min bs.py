def findMin(nums):
    l,r=0,len(nums)-1
    if nums[l]<nums[r]:
        return nums[0]

    while l<r:
        mid=(l+r)//2
        
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid]< nums[mid-1]:
            return nums[mid]
        elif nums[mid]>=nums[l]:
            l=mid+1
        elif nums[mid]<=nums[r]:
            r=mid-1
        


# nums=[4,5,6,7,8,1,2]
# nums=[2, 3, 4, 5, 1]
# nums=[11,12,13,14]
nums=[4,5,1,2,3]

print(findMin(nums))