# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

nums=[1,2,3,4]

res=[0 for i in range(len(nums))]

prefix_product=1
postfix_product=1

for i in range(len(nums)):
    res[i] =prefix_product
    prefix_product *=nums[i] 

# print(res)
# # simple approch
# res2=[0 for i in range(len(nums))]
# for i in range(len(nums)-1,-1,-1):
#     res2[i]=postfix_product
#     postfix_product *=nums[i]

# final=[0 for i in range(len(nums))]
# for i in range(len(nums)):
#     final[i]=res[i]*res2[i]

# print(final)

for i in range(len(nums)-1,-1,-1):
    res[i] *=postfix_product
    postfix_product *=nums[i]

print(res)
