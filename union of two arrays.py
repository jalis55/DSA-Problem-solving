arr1=[1,2,3,4]
arr2=[4,5,6]
s=set()

for i in arr1:
    s.add(i)
for i in arr2:
    s.add(i)

print(s)
# alternative
print(list(set(arr1+arr2)))