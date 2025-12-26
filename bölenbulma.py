sayi = int(input("Bir sayı girin: "))

print("Bölenleri:")
for i in range(1, sayi + 1):
    if sayi % i == 0:
        print(i)
