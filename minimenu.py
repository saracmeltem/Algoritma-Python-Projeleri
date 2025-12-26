while True:
    print("\n--- MİNİ MENÜ ---")
    print("1- Tek / Çift Kontrol")
    print("2- Asal Sayı Kontrol")
    print("3- Hesap Makinesi")
    print("4- Çıkış")

    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        sayi = int(input("Bir sayı girin: "))
        if sayi % 2 == 0:
            print("Sayı çifttir.")
        else:
            print("Sayı tektir.")

    elif secim == "2":
        sayi = int(input("Bir sayı girin: "))
        if sayi <= 1:
            print("Asal değildir.")
        else:
            for i in range(2, int(sayi ** 0.5) + 1):
                if sayi % i == 0:
                    print("Asal değildir.")
                    break
            else:
                print("Asal sayıdır.")

    elif secim == "3":
        sayi1 = float(input("Birinci sayı: "))
        sayi2 = float(input("İkinci sayı: "))
        print("Toplam:", sayi1 + sayi2)
        print("Fark:", sayi1 - sayi2)
        print("Çarpım:", sayi1 * sayi2)
        if sayi2 != 0:
            print("Bölüm:", sayi1 / sayi2)
        else:
            print("0'a bölme hatası!")

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Tekrar deneyin.")
