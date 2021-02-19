from collections import deque


def reverse(queue):
    new_queue = deque()
    while queue:
        #queueからpopされたものをnew_queueに入れていく
        new_queue.append(queue.pop())
    return new_queue


q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(reverse(q))
