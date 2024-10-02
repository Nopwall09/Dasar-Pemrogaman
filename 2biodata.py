RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

print(RED + "\n--- Isi Biodata Anda ---")
nama = (input("Masukkan Nama= "))
alamat = (input("Masukkan Alamat= "))
usia = int (input("Masukkan Usia= "))
no_hp = int (input("Masukkan No. HP= "))
jurusan = (input("Masukkan Jurusan= ") + RESET)

print(BLUE + "\n--- Identitas Mahasiswa ---")
print("Nama    : ", nama)
print("Alamat  : ", alamat)
print("Usia    : ", usia )
print("No. HP  : ", no_hp)
print("Jurusan : ", jurusan)
print("--------------------------" + RESET)