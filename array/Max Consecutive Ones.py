nums = [1, 0, 1, 1, 0, 1]
result = 0
l = 0

for i in nums:
    if i == 1:
        l += 1
    else:
        result = max(result, l)
        l = 0

print(result)
