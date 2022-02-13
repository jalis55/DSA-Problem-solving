lst=[1,3,5,2,4,1]
i=0
sorted_lst=[]
min=lst[0]
while True:
    if i>len(lst) or lst ==[]:
        break

    if i==len(lst):
        print(i)
        sorted_lst.append(min)
        print(sorted_lst)
        lst.remove(min)
        print(lst)
        min=lst[0]
        i=0
        continue
    if min>lst[i]:
        min=lst[i]
        


    i +=1

print(sorted_lst)
