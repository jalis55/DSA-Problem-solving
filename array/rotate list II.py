arr=[1,2,3,4]
#output [4,1,2,3]
rotation=3

for _ in range(rotation):
    x=arr.pop()
    arr.insert(0,x)

print(arr)
