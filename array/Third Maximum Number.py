# nums = [3,2,1]
nums = [2,2,3,1]
nums=list(set(nums))
print(nums)

nums.sort()

if nums[2]:
    print(nums[2])
else:
    print(nums[1])
