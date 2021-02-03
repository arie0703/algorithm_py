from typing import List
import random

def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    #初期値はTrue
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        #swapedが一度もtrueにならなかった時、ループ終了。
        if not swapped:
            break

        swapped = False
        end = end - 1

        #後ろからループスタート
        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start = start + 1
            
    return numbers

        
nums = [random.randint(0, 1000) for i in range(10)]
print(cocktail_sort(nums))