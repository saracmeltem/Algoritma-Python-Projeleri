def bki_hesapla(kilo, boy):
    return kilo / (boy ** 2)

def bki_siniflandirma(bki):
    if bki < 18.5:
        return "Zayıf"
    elif 18.5 <= bki < 25:
        return "Normal"
    elif 25 <= bki < 30:
        return "Fazla kilolu"
    else:
        return "Obez"


while True:
    print("\n=== Boy Kilo Endeksi Hesaplama ===")

    try:
        boy = float(input("Boy (m veya cm): "))
        if boy > 3:  # cm girilirse metreye çevir
            boy /= 100

        kilo = float(input("Kilo (kg): "))

    except ValueError:
        print("❌ Lütfen sayı gir!")
        continue

    bki = bki_hesapla(kilo, boy)
    durum = bki_siniflandirma(bki)

    print(f"\n📊 BKİ: {round(bki, 2)}")
    print(f"📌 Durum: {durum}")

    if durum == "Zayıf":
        print("➡ Kuru tahta! 🍂")
    elif durum == "Normal":
        print("➡ Fıstık gibisin! 🌰🔥")
    elif durum == "Fazla kilolu":
        print("➡ Ekmek yeme! 🍞🚫")
    else:
        print("➡ Balina! 🐋 (Hadi spora!)")

    devam = input("\nTekrar hesaplamak ister misin? (E/H): ").lower()
    if devam != "e":
        print("Program kapatıldı. Görüşürüz! 👋")
        break
