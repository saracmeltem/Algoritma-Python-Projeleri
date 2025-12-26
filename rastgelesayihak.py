import random

# BAŞLA
BS = random.randint(1, 99)  # Rastgele sayı
S = 0                      # Sayaç (hak sayısı)
MAX_HAK = 3

while S < MAX_HAK:
    tahmin = int(input("Tahmininizi girin: "))
    S += 1

    if tahmin > BS:
        print("Daha küçük sayı gir")
    elif tahmin < BS:
        print("Daha büyük sayı gir")
    else:
        print(f"Tebrikler! {S}. tahmininizde bildiniz 🎉")
        break
else:
    print("Haklarınız bitti")
    print(f"Tutulan sayı: {BS}")

# DUR


