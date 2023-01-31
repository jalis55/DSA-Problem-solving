# nums=[3,4,5,1,2]
# nums = [11, 13, 15, 17]
# nums=[4,5,6,1,2,3]
# nums=[4, 5, 6, 7, 0, 1, 2]
nums=[3, 1, 2]
# nums=[2, 3, 4, 5, 1]
# left=0
# right=len(nums)-1

def findMin(nums,l,r):
    mid=(l+r)//2
    
    while l<r:
        if nums[mid]>nums[r]:
            l=mid+1
        elif nums[mid]<nums[r]:
            r=mid
        else:
           return nums[r]
    return nums[l]
        


print(findMin(nums,0,len(nums)-1))
