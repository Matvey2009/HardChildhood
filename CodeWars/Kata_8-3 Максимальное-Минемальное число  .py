def high_and_low(numbers):
    numbers = numbers.split()
    arr = []
    for i in numbers:
        arr.append(int(i))

    xmin = min(arr)
    xmax = max(arr)

    return str(xmax) + " " + str(xmin)
    
# Для локального запуска
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
input()