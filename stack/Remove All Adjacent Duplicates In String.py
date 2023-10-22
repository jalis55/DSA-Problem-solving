s = "abbaca"

stack=[]
for i in s:
    if not stack:
        stack.append(i)
    else:
        if stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)

# for i in s[1:]:
#   if i==stack[-1]:
#     stack.pop()
#   else:
#     stack.append(i)
    
print(stack)