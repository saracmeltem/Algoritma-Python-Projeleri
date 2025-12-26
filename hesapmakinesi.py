sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("Toplama (+)")
print("Çıkarma (-)")
print("Çarpma (*)")
print("Bölme (/)")

islem = input("Yapmak istediğiniz işlemi seçin: ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Bir sayı 0'a bölünemez!")
else:
    print("Geçersiz işlem seçimi.")
