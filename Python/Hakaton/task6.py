#ДОРЕШИВАНИЕ
arr = input()
arr2 = {}

for i in range(len(arr)-2):
    temp = arr[i] + arr[i+1] + arr[i+2]
    S = arr.count(temp)
    arr2[temp] = S
arr = []
nup = []
for i in arr2:
    arr.append(i) 
    nup.append(str(arr2[i]))
    
print(','.join(arr) + ',' + ','.join(nup))