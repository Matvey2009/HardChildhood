Z = input()
W = input()
C = 0
for i in 'qwertyuiopasdfghjklzxcvbnm':
    if i in Z and i in W:
        C += 1 
    
print(C)