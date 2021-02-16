import hashlib
from typing import Any

class HashTable(object):

    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        #ハッシュ生成
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end= ' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')
            
            print()

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    def __getitem__ (self, key) -> Any:
        return self.get(key)

 

hash_table = HashTable()
hash_table.add('car', 'toyota')
hash_table.add('car', 'Nissan')
hash_table.add('pc', 'windows')
hash_table.add('drink', 'cola')
hash_table['sns'] = 'twitter'
hash_table.print()
print(hash_table.get('drink'))