# solution -1
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

while True:
    if val not in nums:
        break
    else:
        nums.remove(val)

print(nums)

# solution 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

while val in nums:
    nums.remove(val)

print(nums)
