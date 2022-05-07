nums = [-2,0,-1]

product=1
max_product=0

for i in nums:
    product *=i
    print(product)
    max_product=max(max_product,product)

# print(max_product)