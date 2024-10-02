def program_awal():
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

    print(BLUE+"\n=====MASUKKAN DETAIL BARANG YANG INGIN DIPILIH=====")


    nama = input("Masukkan nama barang:") #memasukkan input berupa string
    jenis = input("Jenis barang:") #memasukkan input berupa string
    jumlah = int (input("Jumlah barang:")) #memasukkan input berupa integer
    berat = eval(input("Berat(kg):")) #memasukkan input berupa integer
    lebar = eval(input("Lebar barang(cm):")) #memasukkan input berupa integer
    panjang = eval(input("Panjang barang(cm):")) #memasukkan input berupa integer
    #menghitung total luas barang
    total_luas= lebar * panjang
    #cek input
    cek = input(RED +("Apakah barang anda sudah sesuai(ya/tidak)")+RESET).lower()

    if cek == "ya":
        hasil(nama, jenis, jumlah, berat, total_luas)
    elif cek == "tidak":
        print("Kembali ke menu awal")
        program_awal()
    else:
        print("Input tidak dikenali")
        program_awal()

def hasil(nama, jenis, jumlah, berat, total_luas):
    print("\n=====Detail Barang=====")
    print("Nama Barang:", nama)
    print("Jenis Barang:", jenis)
    print("Jumlah:", jumlah)
    print("Berat:", berat)
    print("Total Keseluruhan:", total_luas)


    
program_awal()