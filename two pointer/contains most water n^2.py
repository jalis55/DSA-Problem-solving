water=[1,8,6,2,5,4,8,3,7]

max_area=0

for w1 in range(len(water)):
    for w2 in range(len(water)):
        # w=water.index(w2)-water.index(w1)
        w=w2-w1
        # h=min(w1,w2)
        h=water[w1] if water[w1]<water[w2] else water[w2]

        area=w*h
        # max_area=max(max_area,area)
        max_area=max_area if max_area >area else area
    

print(max_area)