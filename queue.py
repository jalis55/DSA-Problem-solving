class Queue():
    def __init__(self) -> None:
        self.queue=list()
    
    def is_empty(self):
        if len(self.queue)==0:
            print("Empty queue")
            return
    
    def enqueue(self,data):
        self.queue.append(data)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def front(self):
        self.is_empty()
        return self.queue[0]
    def rare(self):
        self.is_empty()
        return self.queue[len(self.queue)-1]

q=Queue()

for i in range(6):
    q.enqueue(i)

q.dequeue()
print(q.front())
print(q.rare())
