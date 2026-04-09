num = int(input("Introduce el número del dado:"))
if num>0 and num <7:
    if num == 1:
        print("6")
    elif num == 2:
        print("5")
    elif num == 3:
        print("4")
    elif num == 4:
        print("3")
    elif num == 5:
        print("2")
    elif num == 6:
        print("1")
else:
    print("ERROR: número incorrecto.")