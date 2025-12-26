import random

# BAŞLA
n = int(input("Deneme sayısını giriniz (n): "))
m = 0  # çember içinde kalan noktaların sayısı

for i in range(1, n + 1):
    # x ve y değerlerini -1 ile 1 arasında rastgele üret
    x = 2 * random.random() - 1
    y = 2 * random.random() - 1

    # x^2 + y^2 ≤ 1 kontrolü
    if x**2 + y**2 <= 1:
        m = m + 1

# Pi hesaplama
pi = 4 * m / n

print("Yaklaşık π değeri:", pi)

# DUR
