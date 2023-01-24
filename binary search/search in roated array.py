



def search(nums,target,left,right):
    if left<=right:
        mid=(left + right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>nums[left]:
            if nums[mid]>target and nums[left]<target:
                search(nums,target,left,mid-1)
            else:
                search(nums,target,mid+1,right)
        else:
            if nums[mid]<target and nums[right]>target:
                search(nums,target,mid+1,right)
            else:
                search(nums,target,left,mid-1)
    else:
        return -1



if __name__=="__main__":
    nums = [4,5,6,7,0,1,2]
    target = 5
    print(search(nums,target,0,len(nums)-1))


