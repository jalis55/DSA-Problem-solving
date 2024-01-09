def two_sum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        num=target-nums[i]
        if num in hashmap:
            return(hashmap[num],i)
        else:
            hashmap[nums[i]]=i



nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))