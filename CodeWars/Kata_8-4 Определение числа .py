def order(sentence):
    sentence = sentence.split()
    arr = sentence.copy()
    for pos in range(1, len(arr)+1):
        for i in sentence:
            for j in range(len(i)):
                if i[j] == str(pos):
                    arr[pos-1] = i
    return " ".join(arr)
    
    
# Для локального запуска
print(order("is2 Thi1s T4est 3a"))
input()

#Идеальный вареант
#order = lambda xs: ' '.join(sorted(xs.split(), key=min))