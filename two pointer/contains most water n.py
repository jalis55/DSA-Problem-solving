water=[1,8,6,2,5,4,8,3,7]
water=[1,1]

left=0
right=len(water)-1
max_area=0

print(left,right)

while left < right:
    w=(right+1)-(left+1)
    h=0
    if water[left] < water[right]:
        h=water[left]
        left +=1
    else:
        h=water[right]
        right -=1
    area=w*h
    max_area=max_area if max_area>area else area

print(max_area)
