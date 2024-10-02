hasil = (5>6) and (10<=8)
print(hasil) #output: False, karena kedua kondisi adalah False

hasil=("saya pinter" == "saya pintar") or (10<=8)
print(hasil)#output: False, karena kedua kondisi adalah False

hasil = not(10<10)
print(hasil) #output: True, karena hasil False dibalik menjadi True
hasil=("saya pinter" == "saya pintar") and (10<=8) or (1!=1)
print(hasil) #output: False, karena semua kondisi adalah False