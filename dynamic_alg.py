
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

class MatrixWrongSizeException(Exception):
    def __str__(self):
        return 'Wrong matrix size'

    __repr__ = __str__


def matrix_multiply(matr1, matr2):
    res_matr = [[0 for _ in range(size_columns(matr2))] for _ in range(size_rows(matr1))]
    for i in range(len(matr1)):
        for j in range(len(matr2[0])):
            for k in range(len(matr2)):
                res_matr[i][j] += matr1[i][k] * matr2[k][j]
    return res_matr

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

print(matrix_multiply(X, Y))

