N = int(input())

arr1 = []
arr2 = []

for i in range(N):
    string = input()
    for j in range(N):
        if (j + i) % 2 == 0:
            arr1.append(string[j])
        else:
            arr2.append(string[j])
            
            
            
        
print(arr1)
print(arr2)