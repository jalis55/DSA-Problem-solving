# nums=[4,5,6,7,0,1,2]
# nums=[3,1,2]
# nums=[1,2,3,4]
nums=[4,1,2,3]
# nums=[4,5,6,7]

def findMax(nums):
    l,r=0,len(nums)-1
    while l<r:
        m=(l+r)//2
        if nums[m]<nums[l]:
            r=m-1
        else:
            l=m+1

    return nums[r]

print(findMax(nums))