sayi = int(input("Bir sayı girin: "))

if sayi <= 1:
    print("Asal değildir.")
else:
    asal = True
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            asal = False
            break

    if asal:
        print("Asal sayıdır.")
    else:
        print("Asal değildir.")
