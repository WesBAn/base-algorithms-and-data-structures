import random
from sorts.quicksort_module import swap


def partition(arr, p, r):
    x = arr[random.randint(p, r)]
    i = p - 1
    j = r + 1
    while True:
        j = j - 1
        while j >= p and arr[j] > x:
            j -= 1
        i = i + 1
        while i <= r and arr[i] < x:
            i += 1
        if i < j:
            swap(arr, i, j)
        else:
            return j



def fst_find_med(arr, k, p, r):
    if p < r:
        q = partition(arr, p, r)
        if q == k:
            return arr[q]
        elif q > k:
            return fst_find_med(arr, k, p, q)
        else:
            return fst_find_med(arr, k, q+1, r)
    elif p == r == k:
        return arr[p]



if __name__ == '__main__':
    a = [34, 71, 51, 79, 89]
    print(a)

    print(fst_find_med(a, len(a)//2, 0, 4))





# def find_med(arr, k):
#     med_lst = []
#     i = 0
#     for i in range(len(arr)//5):
#         arr[i: i+5] = sorted(arr[i: i+5])
#         med_lst.append(arr[i+2])
#     arr[]