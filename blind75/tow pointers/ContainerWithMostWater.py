# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

height = [1,8,6,2,5,4,8,3,7]

max_area=0

#Brute Force approch
for i in range(len(height)):
    for j in range(i+1,len(height)):
        min_height=min(height[i],height[j])
        area=min_height*(j-i)
        max_area=max(max_area,area)
print("Brute Force output")
print(max_area)

# two pointer 

maximum_area=0
l=0
r=len(height)-1

while l<r:
    w=r-l
    h=min(height[l],height[r])
    if height[l]>height[r]:
        r -=1
    elif height[l]<height[r]:
        l +=1
    else:
        l +=1
    maximum_area=max(maximum_area,w*h)
print("Two pointer output")
print(maximum_area)
