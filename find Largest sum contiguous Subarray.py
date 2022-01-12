arr=[-5,4,6,-3,4,-1]

max_sum=0
cur_sum=0

for i in arr:
    cur_sum=cur_sum+i
    max_sum=max(cur_sum,max_sum)
    if cur_sum < 0:
        cur_sum=0

print(max_sum)
