def fibo(n, k):
    f = [None] * n;
    f[0] = 1;
    f[1] = 1;

    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2] * k;

    return f[n-1];

print(fibo(30, 2))