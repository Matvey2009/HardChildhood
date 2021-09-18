K = list(map(int, input()))
M = 1
N = 0

for i in reversed(K):
    M, N = N, M 
    M = i * N + M

print(str(M) + '/' + str(N))
