def task1():
    fst, count = set(input()), 0
    for ch in input():
        if ch in fst:
            count += 1
    print(count)

def task2():
    n, count, count1 = int(input()), 0, 0
    for _ in range(n):
        if int(input()) == 1:
            count1 += 1
        else:
            if count1 > count:
                count = count1
            count1 = 0
    print(count if count > count1 else count1)

# Ne prohodit po vremeni, analog na c++ prohodit wtf?
def task3():
    prev = None
    for _ in range(int(input())):
        x = int(input())
        if x != prev:
            print(x)
            prev = x


def task4():
    def generate(n, cur, opened, closed):
        if len(cur) == 2*n:
            print(cur)
        if opened < n:
            generate(n, cur+'(', opened+1, closed)
        if opened > closed:
            generate(n, cur+')', opened, closed+1)
    generate(input(), '', 0, 0)

def task5():
    print(1 if __import__('collections').Counter(input()) == __import__('collections').Counter(input()) else 0)


def task6():
    import heapq
    def merge(arr1, arr2):
        res_arr = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res_arr.append(arr1[i])
                i += 1
            else:
                res_arr.append(arr2[j])
                j += 1
        if j == len(arr2):
            res_arr.extend(arr1[i:])
        else:
            res_arr.extend(arr2[j:])
        return res_arr
    result = []
    for _ in range(int(input())):
        result = merge(result, [int(i) for i in input().split()][1:])
    print(*result)

task4()

