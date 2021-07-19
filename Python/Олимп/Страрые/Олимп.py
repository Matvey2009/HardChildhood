def test(o):
    a1, b1, a2, b2 = o.split()
    
    a1, b1, a2, b2 = int(a1), int(b1), int(a2), int(b2)
    
    if a1 > b1:
        max1 = a1
    else:
        max1 = b1
    
    if a2 > b2:
        max2 = a2
    else:
        max2 = b2
    H = max1 + max2

    return H

# Для локального запуска
print(test("1 3 2 2")) #5
input()