def get_sum(a,b):
    r = 0
    if a > b:
        maxi = a
        mini = b
    else:
        maxi = b
        mini = a
    
    if a == b:
        print(a)
    else:
        for i in range(mini, maxi+1):
            r += i
    return r

# Для локального запуска
print(get_sum(0,1))
input()