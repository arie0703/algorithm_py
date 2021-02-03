from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            if numbers[j] > numbers[j + 1]:
                #入れ替える
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


nums = [2, 5, 1, 0, 7, 5]
print(bubble_sort(nums))