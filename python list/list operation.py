lst=list(range(10))

# copy list
lst2=lst
print(lst2)
lst2[2]=44
print(lst2)
print(lst)

lst3=lst.copy()
lst4=lst[:]

print(lst3)
print(lst4)
lst3[-1]='x'
lst4[-1]='y'
print(lst3)
print(lst4)

# reverse list
print(lst[::-1])
# print last to n 
print(lst[:4:-1])
