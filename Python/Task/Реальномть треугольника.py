#
while True:
    print("      _ _             _ _      ")
    print("     |   |           |   |     ") 
    print("     |_ _|           |_ _|     ") 
    print("                               ") 
    print("  _ _                     _ _  ") 
    print(" |   |_ _ _ _ _ _ _ _ _ _|   | ") 
    print(" |_                         _| ") 
    print("   | _ _ _ _ _ _ _ _ _ _ _ |   ") 
    print("                               ") 
    a = input("Ведите первое число\n")
    b = input("Ведите второе число\n")
    c = input("Ведите третие число\n")
    if a + b < c or c + a < b or b + c < a:
        print("Эти числа подходят для треугольника -")
    else:
        print("Эти числа не подходят для треугольника -")
    
input()