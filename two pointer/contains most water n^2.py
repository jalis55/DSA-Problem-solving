water=[1,8,6,2,5,4,8,3,7]

max_area=0

for w1 in water:
    for w2 in water:
        w=water.index(w2)-water.index(w1)
        # h=min(w1,w2)
        h=w1 if w1<w2 else w2

        area=w*h
        # max_area=max(max_area,area)
        max_area=max_area if max_area >area else area
    

print(max_area)