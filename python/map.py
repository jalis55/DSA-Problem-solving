
# double the number
lst=list(range(1,20,2))

new_lst=[]

def make_double(i):
    return i+i

for l in lst:
    new_lst.append(make_double(l))

print(new_lst)


# using map
result=list(map(make_double,lst))
print(result)

# using lambda

result2=list(map(lambda x:x+x,lst))

print(result2)