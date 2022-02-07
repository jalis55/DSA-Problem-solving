from inspect import stack


class Stack():
    def __init__(self):

        self.stack=list()
    
    def push(self,data):
        self.stack.append(data)

  
    def is_empty(self):
        if self.stack is None:
            print("Empty stack")
            return


    def pop(self,data):
        self.is_empty()
        self.stack.pop()

    
    def print_stack(self):
        print(self.stack)
    def top(self):
        return self.stack[len(self.stack)-1]


stack=Stack()
lst=list(range(1,11,2))
for i in lst:
    stack.push(i)
stack.print_stack()
print(stack.top())

