def konversi(nilai):
    if nilai >= 90:
        return 'A'
    elif nilai >= 75:
        return 'B'
    elif nilai >= 60:
        return 'C'
    else:
        return 'D'
    
daftar_nilai = [95, 85, 70, 55, 30]
for n in daftar_nilai:
    print(f'Nilai: {n} -> Grade: {konversi(n)}')
        
