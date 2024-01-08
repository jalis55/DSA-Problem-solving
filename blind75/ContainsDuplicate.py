# Input: nums = [1,2,3,1]
# Output: true

# simple approch
# def check_duplicate(nums):
#     return len(nums)==len(set(nums))

def check_duplicate(nums):
    hashmap=set()
    for num in nums:
        if num in hashmap:
            return True
        else:
            hashmap.add(num)

    return False


print(check_duplicate([1,2,3,1]))

