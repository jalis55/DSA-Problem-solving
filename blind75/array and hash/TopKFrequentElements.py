# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
nums = [1,1,1,2,2,3]
k = 2
hashmap={}
for num in nums:
    hashmap[num]=1+hashmap.get(num,0)
print(hashmap)

# need to learn about heap