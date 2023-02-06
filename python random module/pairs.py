import random as rand

b=['x','y','z']
g=['a','b','c']

rand.seed(3)
for _ in range(5):
    rand.shuffle(b)
    rand.shuffle(g)

pair=[rand.choice(b),rand.choice(g)]
print(f"The pair is:{pair}")