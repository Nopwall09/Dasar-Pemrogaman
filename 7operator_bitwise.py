#angka dalam biner
a=10 #1010 dalam biner
b=4  #0100 dalam biner
#operator bitwise and
result_or= a&b #1010 &010=0000(0 dalam desimal)
print("AND:", result_or) 
#operator bitwise OR
print("OR", result_or) #1010|0100=1110(14 dalamdesimal)
#operator bitwise XOR
print("XOR", result_or) #1010^0100=1110(14 dalam desimal)
#operator bitwise NOT
result_not=~a #NOT 1010=............11110101(two' complement)
#operator bitwise shift kiri
result_shift_kiri=a<<1 #1010 <<2=101000(10 dalam desimal)
print("shift kiri:", result_shift_kiri)
#operator bitwise shift kanan
result_shift_kanan=a>>1 #1010 >>21=0010(5 dalam desimal)
print("shift kiri:", result_shift_kanan)
