from collections import Counter
import heapq
from typing import List

#文字列の出現回数のheap

def top_n_with_heap(words: List[str], n: int) -> List[str]:

    counter_word = Counter(words)
    # dictionary {python: 3, c: 2, go: 2, java: 1}
    data = [(-counter_word[word], word) for word in counter_word]
    heapq.heapify(data)
    #print(data)
    return [heapq.heappop(data)[1] for _ in range(n)]

w = ['python', 'c', 'java', 'go', 'python', 'go', 'c', 'python']
print(top_n_with_heap(w, 3))
