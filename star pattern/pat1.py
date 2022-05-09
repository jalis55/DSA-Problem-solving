n=5

print("Pattern -1")
for i in range(n):
    for j in range(i+1):
        print('*',end="")
    print()

print()

print("Pattern-2")
for i in range(n):
    for j in range(i,n):
        print('*',end='')
    print()

print("Patern-3")

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    print()


print("Pattern-4")

for i in range(n):
    for k in range(i+1):
        print(' ',end='')
    for j in range(i,n):
        print("*",end='')


    print()

print("Pattern-5")

for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    for l in range(i+1):
        print('*',end='')
    print()

print("Pattern-6")
for i in range(5):
    for i in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for k in range(i,n):
        print('*',end='')
    print()

print("Pattern 7")

for i in range(n-1):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i):
        print('*',end='')
    for l in range(i+1):
        print('*',end='')
    print()
for i in range(5):
    for i in range(i+1):
        print(' ',end='')
    for j in range(i,n-1):
        print('*',end='')
    for k in range(i,n):
        print('*',end='')
    print()

print("Pattern-8")

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    for k in range(i,n):
        print(' ',end='')
    
    for j in range(i+1):
        print('*',end='')

    for k in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')

    for k in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')

        
    for k in range(i,n):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')

    print()



