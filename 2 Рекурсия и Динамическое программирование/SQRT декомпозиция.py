from math import sqrt, ceil
# Предрасчет:
"""Мы делим массив на чанки колличеством корень от N
   и находим минимальное значение в каждом чанке. 
   После добавляем каждый минимум а одельный массив"""


arr: list = [1, 5, 2, 4, 6, 1, 4, 5, 7, 0]
n: int = len(arr)
memory: list = [0] * int(sqrt(n))
chunk: int = 0
for left in range(0, n-1, int(sqrt(n))):
    minimum = arr[left]
    for right in range(left+1, left + int(sqrt(n))):
        if minimum > arr[right]:
            minimum = arr[right]
    memory[chunk] = minimum
    chunk += 1

def minimum(left, right):
    """"""
    left_up = ceil(left / sqrt(n)) #
    right_down = int(right / sqrt(n))
    ans = arr[left]
    for i in range(left, int(left_up * sqrt(n))):
        if arr[i] < ans: ans = arr[i]
    for j in range(left_up, right_down):
        if ans > memory[j]: ans = memory[j]
    for k in range(int(right_down * sqrt(n)), right):
        if ans > arr[k]: ans = arr[k]
    return ans

print(minimum(2, 10))
