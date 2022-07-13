def high(x):
    arr = list(x.split(" "))
    maxi = 0
    for i in arr:
        summ = 0
        for j in i:
            #print(j, ord(j) - 96)
            summ += (ord(j) - 96)
        if (summ > maxi):
            maxi = summ
            word = i
    return word;

print(high("a b c d e f g h i j k l m n o p q r s t u v w x y z"))
input()