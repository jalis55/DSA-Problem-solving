# nums = [1,3,-1,-3,5,3,6,7]
nums=[1]
k = 3

# Output: [3,3,5,5,6,7]
output=[]
for i in range(len(nums)):
    l=i+k
    if l== len(nums)+1:
        break
    output.append(max(nums[i:l]))


print(output)