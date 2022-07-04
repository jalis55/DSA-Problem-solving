nums = [2,7,11,15]
target = 18
prevmap={}
for i,n in enumerate(nums):
    diff=target-n
    if diff in prevmap:
        print(prevmap[diff],i)
    else:
        prevmap[n]=i


