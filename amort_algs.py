# Метод группировки
class Stack(list):
    def __init__(self):
        super().__init__()

    def push(self, elem):
        self.append(elem)

    def pop(self):
        return super().pop(len(self)-1) if len(self) > 0 else None

    def stack_empty(self):
        return len(self) == 0

    def multi_pop(self, k):
        while not self.stack_empty() and k != 0:
            self.pop()
            k -= 1


def binary_increment(bin_arr):
    i = 0
    while i < len(bin_arr) and bin_arr[i] == 1:
        bin_arr[i] = 0
        i += 1
    if i < len(bin_arr):
        bin_arr[i] = 1


if __name__ == '__main__':
    a = Stack()
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(5)
    print(a)
    a.multi_pop(3)
