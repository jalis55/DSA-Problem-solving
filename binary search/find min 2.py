def findMin(num):
    first, last = 0, len(num) - 1
    while first < last:
        midpoint = (first + last) // 2
        if num[midpoint] > num[last]:
	        first = midpoint + 1
        else:
            last=midpoint

    return num[first]

# nums=[4,5,1,2,3]
nums=[11,12,13,14]
print(findMin(nums))