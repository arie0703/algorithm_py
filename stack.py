from typing import Any

class Stack(object):

    def __init__(self) -> None:
        self.stack = []

    def push(self, data) -> None:
        self.stack.append(data)

    def pop(self) -> Any:
        if self.stack:
            return self.stack.pop()


stack = Stack()
print(stack.stack)
stack.push(1)
stack.push(2)

print(stack.stack)
print(stack.pop())
print(stack.stack)