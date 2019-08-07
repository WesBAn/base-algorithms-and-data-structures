import random
__all__ = ['create_arr', 'swap']

def create_arr(length=12, size=16):
    return [int(random.random()*size) for _ in range(length)]

def swap(arr: list, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapify(arr: list, heap_size, i):
    l = left(i)
    r = right(i)
    largest = l if heap_size > l and arr[l] > arr[i] else i
    if heap_size > r and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, heap_size, largest)

def build_heap(arr: list, heap_size):
    for i in range(heap_size//2, -1, -1):
        heapify(arr, heap_size, i)
    return arr

def heap_sort(heap_arr, heap_size):
    for i in range(heap_size, 0, -1):
        swap(heap_arr, i-1, 0)
        heapify(heap_arr, i-1, 0)
    return heap_arr

class EmtpyHeap(Exception):
    def __str__(self):
        return 'Empty heap'

    __repr__ = __str__

def heap_extract_max(heap_arr):
    if len(heap_arr) == 0:
        raise EmtpyHeap
    heap_sort(heap_arr, len(heap_arr))
    return heap_arr[0]

def heap_insert(heap_arr, key):
    heap_size = len(heap_arr) + 1
    heap_arr.append('')
    i = heap_size - 1
    while i > 0 and heap_arr[parent(i)] < key:
        heap_arr[i] = heap_arr[parent(i)]
        i = parent(i)
        print('i=',i)
    print(i)
    heap_arr[i] = key

if __name__ == '__main__':
    arr = create_arr(length=20, size=100)
    print(arr)
    arr = build_heap(arr, len(arr))
    print(heap_sort(arr, len(arr)))
    # print(heap_extract_max(arr))
    # print(arr)
    heap_insert(arr, 50)
    print(arr)