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


def task3():
    n, prev = int(input()), None
    for _ in range(n):
        x = int(input())
        if x != prev:
            print(x)
            prev = x


def task4():
    n, arr = int(input()), []
    for i in range(n):
