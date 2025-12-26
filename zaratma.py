import random

while True:
    input("Zar atmak için Enter'a basın...")
    zar = random.randint(1, 6)
    print("Zar sonucu:", zar)

    devam = input("Tekrar atmak ister misiniz? (e/h): ")
    if devam.lower() != "e":
        print("Oyun bitti.")
        break
