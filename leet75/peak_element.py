
nums = [1,2,3,1]

def peakElement(nums):
    low=0
    high=len(nums)-1

    while high >=low:
        mid=(high+low)//2

        if nums[mid-1]<nums[mid]>nums[mid+1]:
            return mid
        
        if nums[mid]<nums[mid+1]:
            low=mid+1
        else:
            high=mid-1
        
    return -1

print(peakElement(nums))
