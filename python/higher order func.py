def hof(fn):
    print(fn.__name__)
    fn()


def greet():
    print("hello")

# calling higher order function
# hof(greet)

# filter function
lst=list(range(1,31))
 
# create filter function
lst=[1,2,3,4,5,6,7,8,9,10]

def get_odd(i):
    if i%2==1:
        return i

def my_filter(fn,lst):
    new_lst=[]
    for i in lst:
        if fn(i):
            new_lst.append(i)
    return new_lst

result=my_filter(get_odd,lst)
print(result)
