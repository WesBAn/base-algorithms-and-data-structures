from dynamic_progs.matrix_mul_dynamic_alg import *
def LCS_length(X, Y):
    c = [[0 for _ in range(len(Y)+1)] for _ in range(len(X)+1)]
    b = [[None for _ in range(len(Y)+1)] for _ in range(len(X)+1)]
    for i in range(len(X)+1):
        for j in range(len(Y)+1):
            if i != 0 and j != 0:
                if X[i - 1] == Y[j - 1]:
                    c[i][j] = c[i-1][j-1] + 1
                    b[i][j] = 0
                elif c[i][j-1] >= c[i-1][j]:
                    c[i][j] = c[i][j-1]
                    b[i][j] = 1
                else:
                    c[i][j] = c[i-1][j]
                    b[i][j] = -1
    return c, b


def LCS_print(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 0:
        LCS_print(b, X, i-1, j-1)
        print(X[i-1], end=' ')
    elif b[i][j] == 1:
        LCS_print(b, X, i, j-1)
    else:
        LCS_print(b, X, i-1, j)


if __name__ == '__main__':
    X = ('A', 'B', 'C', 'B', 'D', 'A', 'B')
    Z = ('B', 'C', 'D', 'B')
    c, b = LCS_length(X, Z)
    # __import__('pprint').pprint(b)
    LCS_print(b, X, len(X), len(Z))