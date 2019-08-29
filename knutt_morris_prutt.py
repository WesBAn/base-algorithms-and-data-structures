from typing import List

def prefix(st: str) -> List:
    pr = [0] * len(st)
    for i in range(1, len(st)):
        k = pr[i-1]
        while k > 0 and st[i] != st[k]:
            k = pr[k-1]
            print(1)
        if st[i] == st[k]:
            k += 1
        pr[i] = k
    return pr

def ind_substr_in_st(st: str, substr: str):
    if not substr:
        return -1
    pref = prefix(substr)
    k = 0
    for i in range(len(st)):
        if st[i] == substr[k] :
            k += 1
        elif k > 0 and substr[pref[k-1]] == st[i]:
            k = pref[k-1] + 1
        else:
            k = 0
        if k == len(substr):
            return i - len(substr) + 1
    return -1


if __name__ == '__main__':
    test = 'abcdabcabcdabcdab'

    test2 = 'abcabefabcdabcdabcekabcdet'

    sub = 'abcdabcek'
    print(test2.index(sub))
    print(ind_substr_in_st(test2, sub))

# assert ind_substr_in_st(test, sub) == test2.index(sub)


