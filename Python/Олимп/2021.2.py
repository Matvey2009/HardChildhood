T = int(input())

for i in range(T):
    N = int(input())
    if round(N**(1.0/3.0))**3 == N:
        print('YES')
    else:
        print('NO') 
    
    # Квадрат 3**2 = 9
    # Куб 2**3 = 8
    # Корень 9**(1.0/2.0) = 3
    # Кор куб 8**(1.0/3.0) = 2