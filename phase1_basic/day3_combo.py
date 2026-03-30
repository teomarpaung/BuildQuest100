print("=== Program Serbaguna BuildQuest ===")

nama = input("Masukan nama kamu: ")
print(f"Halo, {nama}, Selamat datang!")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))    

print(f"Jumlah: {a + b}")
print(f"Selisih: {a - b}")
print(f"Perkalian: {a * b}")
print(f"Rata-rata: {(a + b) / 2}")

umur = int(input("Masukkan umur kamu: "))
if umur >= 18:
    print("Kamu sudah dewasa, siap belajar Python lebih dalam!")
else:
    print("Kamu masih muda, tapi sudah keren mau belajar Python!")
    