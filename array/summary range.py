# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"

nums = [0,1,2,4,5,7]
# start=nums[0]
# prev=nums[0]
# for i in range(1,len(nums)):
#     if prev==nums[i]:



s = []
pre = start = nums[0]
for i in nums[1:]:
    if i - pre != 1:
        s.append(f'{start}->{pre}' if pre - start > 0 else f'{pre}')
        start = i
        pre = i
s.append(f'{start}->{pre}' if pre - start > 0 else f'{pre}')

print(s)




