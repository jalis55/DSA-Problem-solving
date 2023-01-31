# nums=[3,4,5,1,2]
nums = [11, 13, 15, 17]
# nums=[4,5,6,1,2,3]
# nums=[4, 5, 6, 7, 0, 1, 2,3]
# nums=[3, 1, 2]
# nums=[2, 3, 4, 5, 1]
# left=0
# right=len(nums)-1



def findMin(nums):
    l,h=0,len(nums)-1
    while h-1 >l:
        mid=(h+l)//2
        if nums[l]>nums[mid]:
            h=mid
        else:
            l=mid
    if nums[h] > nums[l]:
        return nums[0]
    return nums[h]

print(findMin(nums))
