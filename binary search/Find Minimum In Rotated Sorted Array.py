nums=[3,4,5,1,2]
nums = [11, 13, 15, 17]
nums=[4,5,6,1,2,3]
nums=[4, 5, 6, 7, 0, 1, 2]
nums=[3, 1, 2]
nums=[2, 3, 4, 5, 1]
left=0
right=len(nums)-1

def findMin(nums):
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

print(findMin(nums))
