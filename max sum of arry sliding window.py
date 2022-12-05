lst=[4,2,1,7,8,1,2,8,1,0]
window_size=3
n=len(lst)
cur_sum=0
max_sum=-799943434
for i in range(n):
    if i+3<n:
        cur_sum=sum(lst[i:i+window_size])

        max_sum=max(cur_sum,max_sum)
    else:
        break

print(max_sum)
#not excepted
#Sliding Window Maximum
lst=[1,3,-1,-3,5,3,6,7]
window_size=3
n=len(lst)+1
output=[]
for i in range(0,n):
    print(i)
    if i+window_size<n:
        lst1=lst[i:i+window_size]
        
        output.append(max(lst1))
        
    else:
        break

print(output)        


