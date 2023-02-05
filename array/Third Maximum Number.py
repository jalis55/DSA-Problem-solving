nums = [3,2,1]

prev=-1111
count=0
for i in nums:
    if i in prev:
        nums.remove(i)

print(nums[len(nums)-1])