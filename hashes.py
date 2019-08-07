import random
def hash1(m):
    def answer(x):
        return x % m
    return answer

def hash2(m, A=random.random()):
    def answer(x):
        return int(m*(x*A % 1))
    return answer

class HashTableLinked:
    def __init__(self):
        self.hash_fun = hash1(2001)
        self.arr = [None for _ in range(2001)]

    def insertSet(self, x):
        if self.arr[self.hash_fun(x)] is not None:
            for elem in self.arr[self.hash_fun(x)]:
                if elem == x:
                    return
            self.arr[self.hash_fun(x)].append(x)
        else:
            self.arr[self.hash_fun(x)] = [x]

    def findSet(self, x) -> bool:
        if self.arr[self.hash_fun(x)] is None:
            return False
        else:
            for elem in self.arr[self.hash_fun(x)]:
                if elem == x:
                    return True
            return False

    def deleteSet(self, x):
        if self.arr[self.hash_fun(x)] is not None:
            for elem in self.arr[self.hash_fun(x)]:
                if elem == x:
                    self.arr[self.hash_fun(x)].remove(elem)


def test1():
    Table = HashTableLinked()
    Table.insertSet(1312133113)
    print(Table.findSet(2232))
    print(Table.findSet(2232))
    print(Table.findSet(1312133113))
    Table.deleteSet(1312133113)
    print(Table.findSet(1312133113))


def hash3(m):
    c1 = 9
    c2 = 1
    def answer(x, i):
        return (x % m + c1*i + c2*i*i) % m
    return answer

def hash4(m):
    def answer(x, i):
        return (x % m + i*(1 + x % (m - 2))) % m
    return answer

class HashTableOpenAdress:
    def __init__(self):
        self.hash_fun = hash4(701)
        self.arr = [None for _ in range(2001)]
        self.m = len(self.arr)

    def insertSet(self, x):
        i = 0
        while i != self.m:
            j = self.hash_fun(x, i)
            if self.arr[j] is None:
                self.arr[j] = x
                return j
            else:
                i += 1
        raise KeyError

    def findSet(self, x):
        i = 0
        j = self.hash_fun(x, i)
        while i != self.m and self.arr[j] is not None:
            j = self.hash_fun(x, i)
            if self.arr[j] == x:
                return j
            i += 1
        return None

    def deleteSet(self, x):
        if self.arr[self.hash_fun(x)] is not None:
            for elem in self.arr[self.hash_fun(x)]:
                if elem == x:
                    self.arr[self.hash_fun(x)].remove(elem)