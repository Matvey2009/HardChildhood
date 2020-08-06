# Цикл

x = 0
while x < 3:
    x += 1
    print(x)
    
GameOver = False
while not GameOver:
    x += 1
    if x > 6:
        GameOver = True
    print(x)

# Циклы For: Stop, Start-Stop, Start-Stop-Step.

for i in range(5):
    print(i)
    
for i in range(10,13):
    print(i)
    
for i in range(100, 200, 20):
    print(i)
    

x = [-15, -10, 100, 1000, 1002]
print(x)
print(type (x))
for i in x:
    print(i)
    
for i in "Hello World":
    print(i)
    
    #Цикл в цикле
for i in range(1, 11):
    for j in range(10):
        print(i * j, end = " ")
    print("")

input()