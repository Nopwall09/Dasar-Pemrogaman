buah=["pisang", "mangga", "semangka"]
#menggunakan operator "in"
print("mangga in list buah: ", "mangga" in buah) #output True, karena "mangga" ada dalam list buah
print("mangga in list buah: ", "jeruk" in buah) #output False, karena "jeruk" tidak ada dalam list buah
#menggunakan operator "not in"
print("mangga in list buah: ", "jeruk" not in buah) #output True, karena "jeruk" tidak ada dalam list buah


kalimat ="Helo Word"
#memeriksa karakter atau kata dalam string
print("huruf L in hello word: ", "L" in kalimat) #output False, karena huruf "L" besar tidak ada dalam "Helo Word"
print("huruf L in hello word: ", "W" not in kalimat) #output False, karena huruf "W" ada dalam "Helo Word