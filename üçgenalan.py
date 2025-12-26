# Üçgen alanı 2
import math

a = eval(input("Birinci kenarı giriniz (cm): "))
b = eval(input("İkinci kenarı giriniz (cm): "))
c = eval(input("Aradaki açıyı giriniz (derece): "))

# Python'da sin fonksiyonu radyan beklediği için dereceyi çeviriyoruz
alan = a * b * math.sin(math.radians(c)) / 2

print("\nÜçgenin alanı (cm²): {:.2f}\n".format(alan))