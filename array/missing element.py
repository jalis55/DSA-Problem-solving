arr=[0,1,2,3,4]
# arr=[0,1,3]

for i in range(len(arr)+1):
	if i not in arr:
		print(f"missing number is:{i}")
