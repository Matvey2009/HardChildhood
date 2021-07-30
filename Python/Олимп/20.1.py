N = int(input())
arr = list(map(int, input().split()))

for i in range(N):
    arr[i] = chr(arr[i] % 256)
    
    
print(''.join(arr))