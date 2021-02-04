from typing import List
import random

def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        #最小値のindex とりあえずリストの左端のiを格納
        min_idx = i
        for j in range(i + 1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                #ループが終了する際最後にmin_idxに格納されたjが最小値。
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

        return numbers


nums = [random.randint(0, 1000) for i in range(10)]
print(selection_sort(nums))

        
            
