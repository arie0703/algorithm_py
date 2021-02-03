import random
#コードの可読性向上のために使う
from typing import List

# numbersを大きさ順に並び替える関数
def in_order(numbers: List[int]) -> bool:
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
#    for i in range(len(numbers)-1):
#       if numbers[i] > numbers[i + 1]:  
#            return False
#    return True

def bogo_sort(numbers: List[int]):
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

print(bogo_sort([1, 5, 3, 2, 6]))
#ここで指定した数字の配列が関数のnumbersに渡される。

