arr = input()
N, P, B = map(int, input().split())

for i in range(P-1, P-1 + B*N, B):
    print(int(arr[i:i+B], 2))