import math
#diketahui
jari_jari= 7 #cm
#carilah luas lingkarang tersebut
#Luas = π × r²
print("\n=====Masukkan tinggi dan jari jari===")
input_jari_jari = eval(input("Masukkan Jari-jari : ")) #mengambil input jari-jari dari pengguna


luas = math.pi * input_jari_jari**2  #jari-jari dikuadratkan


print("\n=====Hasil perhitungan luas===")
print("Hasil Luas m²: ", luas)  #menampilkan luas dalam satuan meter persegi
