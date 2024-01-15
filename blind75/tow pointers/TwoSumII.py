# numbers = [2,7,11,15]
# target = 9
# Output: [1,2]

def two_sumII(nums,target):
    f,l=0,len(nums)-1

    while f<l:
        if nums[f]+nums[l]==target:
            return(f+1,l+1)
        elif nums[f]+nums[l]>target:
            l -=1
        else:
            f +=1
    return False


# numbers = [2,7,11,15]
# target = 9
numbers=[2,3,4]
target=6
print(two_sumII(numbers,target))