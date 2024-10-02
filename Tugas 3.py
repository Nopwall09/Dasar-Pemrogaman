#mengkonversi rupiah ke dalam dolar Amerika, yen jepang, dan ringgit Malaysia.
dolar_amerika = 15000
yen_jepang = 105
ringgit_mly = 3500  


#fungsi awal untuk memilih mata uang yang akan dikonversi
def input_awal():
    print("\n=====apa yang ingin anda konversikan=====")

    cek = input("pilih mata uang yangingin anda konversikan : dolar/yen/ringgit : ") #meminta input dari pengguna untuk memilih mata uang
    if cek == "dolar": #memilih fungsi berdasarkan pilihan mata uang
        hasil_dolar_amerika()
    elif cek == "yen":
        hasil_yen_jepang()
    elif cek ==  "ringgit":
        hasil_ringgit()
    else:  #jika input tidak dikenali, meminta pengguna untuk input ulang
        print("input tidak dikenali")
        input_awal()       
 
  

#fungsi untuk mengkonversikan ke dolar
def hasil_dolar_amerika():  
    rupiah = eval (input("Masukkan rupiah yang ingin anda tukar : ")) #input jumlah Rupiah
    dolar = rupiah / dolar_amerika #menghitung konversi ke dolar
    print(f"{rupiah} IDR = {dolar:.2f} USD") #menampilkan hasil konversi
    input_awal() #kembali ke pilihan awal

#fungsi untuk mengkonversikan ke jepag
def hasil_yen_jepang():
    rupiah = eval (input("Masukkan rupiah yang ingin anda tukar : ")) #input jumlah Rupiah
    yen = rupiah / yen_jepang #menghitung konversi ke yen
    print(f"{rupiah} IDR =  {yen:.2f} JPY") #menampilkan hasil konversi
    input_awal() #kembali ke pilihan awal

#fungsi untuk mengkonversikan ke ringgit 
def hasil_ringgit(): 
    rupiah = eval (input("Masukkan rupiah yang ingin anda tukar : ")) #input jumlah Rupiah
    ringgit = rupiah / ringgit_mly  #menghitung konversi ke ringgit
    print(f"{rupiah} IDR = {ringgit:.2f} MLY")  #menampilkan hasil konversi
    input_awal() #kembali ke pilihan awal


input_awal()



    





