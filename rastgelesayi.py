import random

# BAŞLA
BS = random.randint(1, 99)  # Rastgele(99) + 1
S = 0  # sayaç

while True:
    tahmin = int(input("Tahmininizi girin: "))
    S = S + 1

    if tahmin > BS:
        print("Daha küçük sayı gir")
    elif tahmin < BS:
        print("Daha büyük sayı gir")
    else:
        print(f"{S}. tahmininizde bildiniz ")
        break

# DUR



    
        


