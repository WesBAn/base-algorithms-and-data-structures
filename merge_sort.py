from heap_sort import *
arr = create_arr(length=20)
arr[0:10] = sorted(arr[0:10])
arr[10:len(arr)] = sorted(arr[10:len(arr)])
print(arr)

def merge(arr, p, q, r):
    tmp_arr = arr.copy()
    i, j = p, q + 1
    main_ind = p
    while i != q + 1 and j != r + 1:
        if tmp_arr[i] <= tmp_arr[j]:
            arr[main_ind] = tmp_arr[i]
            i += 1
        else:
            arr[main_ind] = tmp_arr[j]
            j += 1
        main_ind += 1
    if j == r + 1:
        arr[main_ind: r + 1] = tmp_arr[i: q + 1]
    else:
        arr[main_ind: r+1] = tmp_arr[j: r+1]


def merge_sort(arr, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

# test_arr = create_arr(length=4)
if __name__ == '__main__':
    test_arr = create_arr(length=24)
    print(test_arr)
    sorted_arr = sorted(test_arr.copy())
    merge_sort(test_arr, 0, len(test_arr)-1)
    print(test_arr)
    print(test_arr==sorted_arr)