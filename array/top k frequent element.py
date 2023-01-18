def topKFrequent(nums, k):
    map={}
    for num in nums:
        if num not in map:
                map[num]=1
        else:
            map[num] +=1
                
    map=dict(sorted(map.items(),key=lambda x:x[1],reverse=True))
    return list(map.keys())[:k]

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums,k))
