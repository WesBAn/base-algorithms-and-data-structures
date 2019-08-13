from typing import List, Tuple
import pprint
import random
random.seed(2)
class MatrixWrongSizeException(Exception):
    def __str__(self):
        return 'Wrong matrix size'

    __repr__ = __str__


def create_random_matrix(n, m, size_one_elem=10):
    return [[random.randint(0,size_one_elem) for _ in range(m)] for _ in range(n)]


def create_empty_matrix(n, m):
    return [[0.0 for _ in range(m)] for _ in range(n)]

def mprint(matr):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in matr]))

def rows(matr):
    return matr if matr[0] else None

def columns(matr):
    if not matr[0]:
        return None
    return [[matr[j][i] for j in range(len(matr))] for i in range(len(matr[0]))]

def size_columns(matr):
    return len(matr[0]) if len(matr) > 0 else 0

def size_rows(matr):
    return len(matr)


def matrix_multiply(matr1, matr2):
    res_matr = [[0 for _ in range(size_columns(matr2))] for _ in range(size_rows(matr1))]
    for i in range(len(matr1)):
        for j in range(len(matr2[0])):
            for k in range(len(matr2)):
                res_matr[i][j] += matr1[i][k] * matr2[k][j]
    return res_matr


def order_m_index_gen(length):
    start_i = 0
    for j in range(1, length):
        for i in range(0, length):
            if j + i < length:
                yield i, j + i
            else:
                break


def order_all_matrix_multiply(sizes_of_matrix: List[Tuple]):
    m = [[0 for _ in range(len(sizes_of_matrix))] for _ in range(len(sizes_of_matrix))]
    s = [[0 for _ in range(len(sizes_of_matrix))] for _ in range(len(sizes_of_matrix))]
    for i, j in order_m_index_gen(len(sizes_of_matrix)):
        m[i][j] = float('inf')
        for k in range(i, j):
            new_div = m[i][k] + m[k+1][j] + sizes_of_matrix[i][0] * sizes_of_matrix[k][1] * sizes_of_matrix[j][1]
            if new_div < m[i][j]:
                m[i][j] = new_div
                s[i][j] = k
    return m, s


def _step_multi_matrix_multiply(lst_matrix, s, i, j):
    if j > i:
        X = _step_multi_matrix_multiply(lst_matrix, s, i, s[i][j])
        Y = _step_multi_matrix_multiply(lst_matrix, s, s[i][j]+1, j)
        return matrix_multiply(X, Y)
    else:
        return lst_matrix[i]

def multi_matrix_multiply(lst_matrix):
    size_of_all_matrix = [(size_rows(i), size_columns(i)) for i in lst_matrix]
    m, s = order_all_matrix_multiply(size_of_all_matrix)
    # mprint(s)
    return _step_multi_matrix_multiply(lst_matrix, s, 0, len(lst_matrix)-1)


if __name__ == '__main__':
    a1 = create_random_matrix(3, 2)
    a2 = create_random_matrix(2, 4)
    a3 = create_random_matrix(4,1)
    # a4 = create_random_matrix(2,8)
    # a5 = create_random_matrix(8,5)
    for num, i in enumerate([a1, a2, a3]):
        print(f'MATRIX A{num+1}=')
        mprint(i)
        print('/MATRIX A/')
    print('res')
    print(multi_matrix_multiply([a1, a2, a3]))

