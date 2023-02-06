# nums = [3,2,1]
nums=[5,2,2]
print(nums[-3])

nums = sorted(list(set(nums)))
if len(nums) > 2:
    print( nums[-3])
else:
    print(nums[-1]) 