nums = [2,7,11,15]
target = 9
prevmap={}
for i,n in enumerate(nums):
    diff=target-i
    if diff in prevmap:
        print(prevmap[diff],i)
    prevmap[n]=i 
    print(prevmap)


