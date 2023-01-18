nums=[1,2,3,4,5]
res=1
for i in range(len(nums)):
    res=res*nums[i]

print(res)

#only even numbers

res=1
for i in range(len(nums)):
    if nums[i]%2==0:
        res=res*nums[i]

print(res)

#difference of even and odd product
even_res=1
odd_res=1
for i in range(len(nums)):
    if nums[i]%2==0:
        even_res=even_res*nums[i]
    else:
        odd_res=odd_res*nums[i]


print("difference:",even_res-odd_res)