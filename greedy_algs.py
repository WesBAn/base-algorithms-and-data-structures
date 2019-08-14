import heapq
from trees import trees
from functools import total_ordering
arr = {'a': 15, 'b': 7, 'c': 6, 'd': 6, 'e':5}
# arr = {'a': 15, 'b': 6, 'c': 6}

@total_ordering
class HuffNode:
    def __init__(self, ch, count_ch, left=None, right=None):
        self.ch = ch
        self.count_ch = count_ch
        self.left = left
        self.right = right

    def walk(self, coded, arr_res):
        if self.left is None and self.right is None:
            # print(self.ch, 'CODED_TO', coded)
            arr_res[self.ch] = coded
            # return self.ch
        else:
            self.left.walk(coded + '0', arr_res)
            self.right.walk(coded + '1', arr_res)

    def __eq__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return self.count_ch == other.count_ch

    def __lt__(self, other):
        if type(other) != type(self):
            return NotImplemented
        return self.count_ch < other.count_ch

def HaffmanEncode(arr):
    l = []
    for item in arr.items():
        l.append(HuffNode(item[0], item[1]))
    print(l)
    heapq.heapify(l)

    while len(l) > 1:
        left, right = heapq.heappop(l), heapq.heappop(l)
        heapq.heappush(l, HuffNode(None, left.count_ch + right.count_ch, left, right))

    return l[0]



l = HaffmanEncode(arr)
res = {}
l.walk('', arr_res=res)
print(res)