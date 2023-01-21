nums = [1,1,1,0,0,0,1,1,1,1,0]
k=2
nums=[0,0,0,0]
#output 6
k = 0
left=0
count={}
res=0
for right in range(len(nums)):
    count[nums[right]]=1+count.get(nums[right],0)
    while (right-left+1)-max(count.values()) >k:
        count[nums[left]] -=1
        left +=1
    res=max(res,right-left+1)

print(res)