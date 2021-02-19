from typing import Any
from collections import deque


class Queue(object):
    def __init__(self) -> None:
        self.queue = []
    
    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)
            # = popleft()


q = Queue()
q.enqueue(1) #append
q.enqueue(2)
q.enqueue(3)
print(q.queue)
q.dequeue()
print(q.queue)