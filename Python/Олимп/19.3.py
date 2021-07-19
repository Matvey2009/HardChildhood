M, N = map(int, input().split())
arr = list(map(int, input().split()))

maxim = 0
for i in arr:
    temp = arr.count(i)
    if temp > maxim:
        maxim = temp

if maxim >= N:
    print(0)
else:
    print(N - maxim)