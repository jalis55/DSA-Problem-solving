# nums = [1,2,3,4]
nums = [3,1,4,2]

for i in range(1,len(nums)-1):
    if  nums[i-1]<nums[i] and nums[i]>nums[i+1] and nums[i+1]>nums[i-1]:
        print("ok")
        break

    