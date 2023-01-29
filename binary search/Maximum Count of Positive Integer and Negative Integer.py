nums = [-2, -1, -1, 1, 2, 3]

neg = len([x for x in nums if x < 0])
pos = len([x for x in nums if x > 0])

# x = max(len([x for x in nums if x < 0]), len(x for x in nums if x > 0))


print(max(neg, pos))
