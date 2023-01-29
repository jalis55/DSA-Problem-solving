nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
key = 8


def binary_search(nums, target, l, r):

    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    return -1


status = binary_search(nums, key, 0, len(nums)-1)
print(status)
