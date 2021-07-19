n = input()
n = int(n)
if n % 4 == 0:
    print(-n)
elif (n+1) % 4 == 0:
    print(0)
elif (n+2) % 4 == 0:
    print(n+1)
else:
    print(1)