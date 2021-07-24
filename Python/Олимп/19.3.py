N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
lest = 0
max_counter = 1
start_counter = 0

for i in arr:
    if i > lest:
        counter = 1
        lest = i
        start_counter = arr.index(i)
    else:
        counter += 1
        if counter >= M:
            max_counter = M
            break
        if counter >= max_counter:
            if start_counter >= M - counter:
                max_counter = counter

print(M - max_counter)