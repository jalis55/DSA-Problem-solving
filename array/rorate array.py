nums = [1,2,3,4,5,6,7]

print(nums[:0])
k = 3
#  [5,6,7,1,2,3,4]

nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]

print(nums)