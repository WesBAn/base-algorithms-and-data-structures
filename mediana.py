import random
from sorts.quicksort_module import swap


def partition(arr, p, r):
    x = arr[random.randint(p, r)]
    i, j = p - 1, r + 1
    while True:
        j, i = j - 1, i + 1
        while j >= p and arr[j] >= x: j -= 1
        while i <= r and arr[i] <= x: i += 1
        if i < j:
            swap(arr, i, j)
        else:
            return j



def fst_find_med(arr, k, p, r):
    if p == r:
        return arr[p]
    if p < r:
        q = partition(arr, p, r)
        i = q-p+1
        if k >= i:
            return fst_find_med(arr, k, p, q)
        else:
            return fst_find_med(arr, k-i, q+1, r)





def fast_statistic(lst: list, i: int) -> int:
    if len(lst) <= 10:
        lst.sort()
        return lst[i]
    chunks = [sorted(lst[i:i+5]) for i in range(len(lst)//5)]
    if len(lst) % 5 != 0:
        lst[len(lst) - (len(lst) % 5):] = sorted(lst[len(lst) - (len(lst)%5) : ])
        chunks.append(lst[len(lst) - (len(lst)%5):])

    medians =[chunk[(len(chunk)-1)//2] for chunk in chunks]
    meds_of_med = fast_statistic(medians, (len(medians)-1)//2)
    L1 = []
    L2 = []
    L3 = []
    for elem in lst:
        if elem < meds_of_med:
            L1.append(elem)
        elif elem > meds_of_med:
            L2.append(elem)
        else:
            L3.append(elem)
    if i < len(L1):
        return fast_statistic(L1, i)
    elif i < len(L1) + len(L3):
        return meds_of_med
    else:
        return fast_statistic(L2, i-len(L1)-len(L3))



if __name__ == '__main__':
    a = [34, 71, 51, 79, 89, 123, 1223, 1,0,1313, 5512,222,3 , 21313,23,12412412]
    print(a)
    print(sorted(a))
    print(fst_find_med(a, len(a)-3, 0, len(a)-1))
    print(fast_statistic(a, len(a)-1))




# def find_med(arr, k):
#     med_lst = []
#     i = 0
#     for i in range(len(arr)//5):
#         arr[i: i+5] = sorted(arr[i: i+5])
#         med_lst.append(arr[i+2])
#     arr[]