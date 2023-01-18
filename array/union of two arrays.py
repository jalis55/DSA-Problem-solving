arr1=[1,2,3,4]
arr2=[4,5,6]
s=set(arr1)

# for i in arr1:
#     s.add(i)
for i in arr2:
    s.add(i)

print(s)
# alternative
union=set(arr1+arr2)
print(union)
