arr=[4, 5, 1, 2,7,3]

min=arr[0]
max=arr[0]

for i in arr:
    if i>max:
        max=i
    if i<min:
        min=i

print(max,min)