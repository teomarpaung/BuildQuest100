def salam(nama):
    print(f"Halo {nama}, selamat datang di BuildQuest!")

salam("Andi")
salam("Sinta")

def hitung_diskon(harga, persen):
    potongan = harga * (persen / 100)
    return harga - potongan

total = hitung_diskon(200000, 10)
print("Total setelah diskon: ", total)
