T = int(input())

for i in range(T):
    N = int(input())
    if round(N**(1.0/3.0))**3 == N:
        print('YES')
    else:
        print('NO')