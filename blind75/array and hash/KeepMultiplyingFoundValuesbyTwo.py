# Input: nums = [5,3,6,1,12], original = 3
# Output: 24

nums = [5,3,6,1,12]
original = 3

for i in range(len(nums)):
    if original in nums:
        original *=2
    else:
        break

print(original)