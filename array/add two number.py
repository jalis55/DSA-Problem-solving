# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1 = [2,4,3]
l2 = [5,6,4]
res_list=[]
carry=0

for i,j in zip(l1,l2):
    res=i+j+carry
    if res>=10:
        res_list.append(res%10)
        carry=1
    else:
        res_list.append(res)
print(res_list)