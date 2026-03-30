pengeluaran = int(input("Masukkan total pengeluaran hari ini (Rp): "))
target = 1000000 # batas harian

if pengeluaran > target:
    print("Kamu melebihi batas harian! Kurangi pengeluaran besok.")
else:
    print("Bagus! Kamu masih dalam batas wajar.")