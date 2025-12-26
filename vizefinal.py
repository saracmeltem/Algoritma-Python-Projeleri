# Kullanıcıdan not girişlerini alalım
vize_notu = float(input("Vize notunuzu giriniz: "))
final_notu = float(input("Final notunuzu giriniz: "))

# Ortalama hesaplama (Vize %40, Final %60)
ortalama = (vize_notu * 0.4) + (final_notu * 0.6)

# Sonucu ekrana yazdıralım
print("-" * 30)
print(f"Yıl Sonu Ortalamanız: {ortalama:.2f}")

# Geçme/Kalma durumunu kontrol edelim
if ortalama >= 50:
    print("Durum: Başarılı, Geçtiniz.")
else:
    print("Durum: Başarısız, Kaldınız.")