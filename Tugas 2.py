import math
#2 × π × r × (r + t)
#π × r² × t
print("\n=====Masukkan tinggi dan jari jari===")
input_tinggi = eval(input("Masukkan Tinggi : "))
input_jari_jari = eval(input("Masukkan Jari-jari : "))

luas = 2 * math.pi * input_jari_jari  * (input_jari_jari + input_tinggi)
volume = math.pi * input_jari_jari** 2 * input_tinggi
print("\n=====Hasil perhitungan luas dan Volume===")
print("Hasil Luas m²: ", luas)
print("Hasil Volume m²: ", volume)










