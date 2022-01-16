# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
s=set()
nums1=[1,2,2,1]
nums2=[1,1]

# output  [9,4]

for i in nums1:
    if i  in nums2:
        s.add(i)

print(s)
