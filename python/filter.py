# return elements based on conditions


def even_numbers(i):
    if i%2==0:
        return i

lst=list(range(1,51))

result=list(filter(even_numbers,lst))

print(result)

# using lambda
result2=list(filter(lambda x:x%2==0,lst))
print(result2)

