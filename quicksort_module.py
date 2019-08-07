import random
from heap_sort import *
def partition(arr, p, r):
    x = arr[random.randint(p, r+1)]
    i = p - 1
    j = r + 1
    while True:
        j = j -1
        while j >= p and arr[j] > x:
            j -= 1
        i = i + 1
        while i <= r and arr[i] < x:
            i += 1
        if i < j:
            swap(arr, i, j)
        else:
            return j


def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q)
        quick_sort(arr, q + 1, r)

arr = create_arr(length=24)
print(arr)
quick_sort(arr, 0, len(arr)-1)
print(arr)