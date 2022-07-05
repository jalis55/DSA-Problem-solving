def sumtwo(numbers,target):
    l,r=0,len(numbers)-1
    while l<r:
        sum=numbers[l]+numbers[r]
        if sum==target:
            return [l+1,r+1]
        elif sum<target:
            l +=1
        else:
            r -=r


print(sumtwo([3,4,5,6,7],11))
