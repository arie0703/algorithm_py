from typing import List

def linear_search(numbers: List[int], value: int) -> int:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return 1
    return -1


# def binary_search(numbers, value):
#     left, right = 0, len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         #ソートの真ん中が指定された値より小さい場合
#         elif numbers[mid] < value:
#             left = mid + 1
#         #ソートの真ん中が指定された値より大きい場合
#         else:
#             right = mid - 1
#     return -1

def binary_search(numbers, value):
    def _binary_search(numbers, value, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else: return _binary_search(numbers, value, left, mid - 1)
    
    return _binary_search(numbers, value, 0, len(numbers) - 1)


nums = [0,2,3,5,7,8,11,15,20,14]
print(binary_search(nums, 8))