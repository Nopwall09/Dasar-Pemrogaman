#fungsi choice
import random
buah = ["apel", "ceri", "jeruk", "mangga", "kiwi"]
print(random.choice(buah)) #memilih buah secara acak dari daftar buah


#fungsi choice randrange
print("Nilai random dari 0 s.d 100 : ", random.randrange(100)) #menghasilkan angka acak antara 0 hingga 99
print("Nilai random dari 50 s.d 100 : ", random.randrange(50,100)) #menghasilkan angka acak antara 50 hingga 99
print("Nilai random dari 50 s.d 100 kelipatan 5 : ", random.randrange(50,100,5))  #menghasilkan angka acak kelipatan 5 antara 50 hingga 99

#fungsi random
from random import random
print(random()) #menghasilkan nilai float acak antara 0.0 hingga 1.0

#fungsi seed
import random 
random.seed(3) #mengatur seed agar nilai random yang dihasilkan konsisten
print(random.randint(1,1000)) #membangkitkan nilai random
random.seed(3)                 #menguncinilai random
print(random.randint(1,1000)) #membangkitkan nilai random
                               #tetap terkunci oleh seed
print(random.randint(1,100))   #membangkitkan nilairandomkembali

#fungsi Shuffle
import random
buah = ["apel", "ceri", "jeruk", "mangga", "kiwi"] #mendifinisikan buah buah
random.shuffle(buah) #mengacak urutan elemen dalam daftar buah
print(buah) #menampilkan daftar buah dengan urutan yang sudah diacak

