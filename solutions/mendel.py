def compl(k, m, n):
    total = k + m + n
    return 1 - (.25 * m * (m-1) + (m * n) + n * (n-1)) / (total * (total-1))


print(compl(22, 30, 28))
