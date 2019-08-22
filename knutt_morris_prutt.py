def prefix(st):
    res = [0]*len(st)
    for num in range(1, len(st)):
        k = res[num-1]
        while k > 0 and st[k] != st[num]:
            k = res[k-1]
        if st[k] == st[num]:
            k += 1
        res[num] = k
    return res

test = 'abcdabcabcdabcdab'

print(prefix(test))

