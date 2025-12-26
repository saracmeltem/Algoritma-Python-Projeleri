def hanoi(n, kaynak, hedef, yardımcı):
    if n == 1:
        print(f"{kaynak} → {hedef}")
        return
    
    # 1. Adım: n-1 diski kaynaktan yardımcıya taşı
    hanoi(n - 1, kaynak, yardımcı, hedef)
    
    # 2. Adım: en büyük diski kaynaktan hedefe taşı
    print(f"{kaynak} → {hedef}")
    
    # 3. Adım: n-1 diski yardımcıdan hedefe taşı
    hanoi(n - 1, yardımcı, hedef, kaynak)


# Kullanıcıdan disk sayısı
n = int(input("Disk sayısı: "))
print("\nHamleler:")
hanoi(n, "A", "C", "B")

# Toplam hamle sayısı
print(f"\nToplam hamle: {2**n - 1}")
8
