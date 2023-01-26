
# def minimum(nums,l,r):
#     if l<r:



nums=[3,4,5,1,2]
nums = [11, 13, 15, 17]
nums=[4,5,6,1,2,3]
left=0
right=len(nums)-1
# print(minimum(nums,0,len(nums)-1))
mid = (left+right)//2
if nums[left]<=nums[mid+1]:
    print(nums[left])
else:
    print(nums[mid+1])