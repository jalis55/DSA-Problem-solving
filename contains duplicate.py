nums = [1,2,14,18,22,1]

hasmap=set()

for num in nums:
    if num in hasmap:
        print("True")
        break
    else:
        hasmap.add(num)


