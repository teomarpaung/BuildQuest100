nilai = int(input("Masukkan nilai ujian: "))

if nilai == 100:
    print("Nilai Sempurna! Kamu jenius!")
elif nilai >=90:
    print("Nilai kamu A. Hebat!")
elif nilai >=75:
    print("Nilai kamu B. Cukup baik!")
elif nilai >=60:
    print("Nilai kamu C. Perlu pelatihan lagi!")
elif nilai >=40:
    print("Nilai kamu D. Ayo ulangi belajar!")
else:    
    print("Nilai kamu E. Jangan menyerah, terus berusaha!")