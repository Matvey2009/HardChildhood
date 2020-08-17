def iq_test(numbers):
    numbers = numbers.split()
    arr = []
    for i in range(len(numbers)):
        arr.append(int(numbers[i]) % 2)
    if arr.count(1) > arr.count(0):
        temp = 0
    else:
        temp = 1
    for i in range(len(arr)):
        if arr[i] == temp:
            return i+1

# Для локального запуска
print(iq_test("2 4 7 8 10"))
input()