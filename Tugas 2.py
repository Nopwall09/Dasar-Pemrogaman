import math
#2 × π × r × (r + t)
#π × r² × t
print("\n=====Masukkan tinggi dan jari jari===")
input_tinggi = eval(input("Masukkan Tinggi : ")) #menerima input tinggi dari pengguna
input_jari_jari = eval(input("Masukkan Jari-jari : ")) #menerima input jari jari dari pengguna

luas = 2 * math.pi * input_jari_jari  * (input_jari_jari + input_tinggi)
volume = math.pi * input_jari_jari** 2 * input_tinggi

print("\n=====Hasil perhitungan luas dan Volume===")
print("Hasil Luas m²: ", luas) # Menampilkan hasil luas
print("Hasil Volume m²: ", volume) # Menampilkan hasil volume










