nums = [1,3,4,2,2]
lst=set()


for i in nums:
    if i in lst:
        dup=i
    else:
        lst.add(i)

print(dup)