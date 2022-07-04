string='[]]'

open='({['
close=')}]'
pp=['()','{}','[]']
stack=[]
valid=True
for p in string:
    if p in open:
        stack.append(p)
    if p in close:
        if len(stack) !=0:
            if stack.pop()+p not in pp:
                valid=False
                break
        else:
            valid=False
            break

if valid==False:
    print("Invalid")
else:
    print("valid")
