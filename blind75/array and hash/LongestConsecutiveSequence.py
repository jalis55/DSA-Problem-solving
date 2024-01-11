# Input: nums = [100,4,200,1,3,2]
# Output: 4

nums = [100,4,200,1,3,2,7,8,9]
# nums = [0,3,7,2,5,8,4,6,0,1]
nums=sorted(set(nums))

cnt=1
max_cnt=1
i=0
while i<len(nums)-1:
    if nums[i+1]-nums[i]==1:
        cnt +=1
    else:
        # cnt=max(cnt,max_cnt)
        cnt =1
    max_cnt=max(cnt,max_cnt)
    i +=1

print(max_cnt)    