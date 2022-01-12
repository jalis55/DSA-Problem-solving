# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

lst=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
j=0

for i in range(len(lst)):
    if lst[i]<0:
        lst[i],lst[j]=lst[j],lst[i]
        j +=1


        
print(lst)