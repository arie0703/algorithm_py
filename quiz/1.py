from typing import List, Tuple, Optional


# リストの中の数字を足して特定の数字になる組み合わせを抽出
def get_pair(numbers, target):
    #cacheに数値を入れる
    cache = set()
    
    for num in numbers:
        cache.add(num)
        val = target - num
        if val in cache:
            return val, num

#リストの中の数字を足して、リストの数字の合計値の半分になるペアを抽出
def get_pair_half_sum(numbers):
    sum_numbers = sum(numbers)

    half_sum, remainder = divmod(sum_numbers, 2)
    if remainder != 0:
        return
        
    # if sum_numbers % 2 != 0:
    #     return
    # half_sum = int(sum_numbers / 2)

    cache = set()
    for num in numbers:
        cache.add(num)
        val = half_sum - num
        if val in cache:
            return val, num
            

l = [11, 2, 5, 9, 10, 3]
t = 12

print(get_pair(l, t))
print(get_pair_half_sum(l))
