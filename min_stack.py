stack=[]
minStack=[]
min=None

def push(val):
	global min
	if not min:
		min=val
		minStack.append(val)
		stack.append(val)
	else:
		if min>=val:
			min=val
			minStack.append(min)
		stack.append(val)
def pop():
	if stack[-1]==minStack[-1]:
		stack.pop()
		minStack.pop()
	else:
		stack.pop()


def top():
	return stack[-1] if stack else None

print(top())

push(2)
push(1)
push(-2)
push(3)

print(stack)
print(minStack)

pop()
pop()
print(stack)
print(minStack)

print(f"Min stack is:{minStack[-1]}")
