# Input: nums = [1,5,0,3,5]
# Output: 3

# def get_min_value(nums):
#     min_value=float('inf')

#     for num in nums:
#         if num != 0 and num < min_value:
#             min_value=num
#     if min_value==float('inf'):
#         return None
#     else:
#         return min_value


get_min=lambda nums:min((num for num in nums if num != 0),default=None)

nums = [1,5,0,3,5]
c=0
for i in range(len(nums)):
    val=get_min(nums)
    if val==None:
        break
    else:
        c +=1
        for j in range(len(nums)):
            if nums[j]==0:
                continue
            else:
                nums[j]=nums[j]-val
print(c)


min_except_zero = lambda arr: min((num for num in arr if num != 0), default=None)

# Example usage
my_array = [3, 0, 7, 1, 0, 9, 2]
result = min_except_zero(my_array)
print("Minimum non-zero value:", result)