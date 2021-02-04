from typing import List
import random

def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            index = index + 1
        
        if numbers[index] >= numbers[index - 1]:
            index = index + 1
        else:
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            #入れ替えが発生したら参照する数字を一個戻すのでindexの数を減らす。
            index = index -1

    return numbers

nums = [random.randint(0, 1000) for i in range(10)]
print(gnome_sort(nums))