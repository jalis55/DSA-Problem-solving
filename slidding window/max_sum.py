

lst=[3,4,2,1,9,7,8,5,6]
k=3


total=sum(lst[:k])
max_sum=total

for i in range(len(lst)-k):
    total=(total-lst[i])+lst[i+k]

    max_sum=max(max_sum,total)

print(max_sum)
