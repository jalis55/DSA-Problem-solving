import random

lst=[i for i in range(20)]

# pick a random number
a_random_number=random.choice(lst)
print(a_random_number)

# seeed
random.seed(7)
  
print(random.random())
print(random.random())

#generate random integer
random_list=[]
for _ in range(10):
    random_list.append(random.randint(1,999))
print(random_list)