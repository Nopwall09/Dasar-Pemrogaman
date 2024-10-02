a=5
b=5
#nilai a dan b sama, dan merujuk ke objek yang sama
print("a is b: ", a is b)           #output=True
print("a is not b: ", a is not b)   #output=False

list1=[1,2,3]
list2=[1,2,3]
#meskipun nilai list1 dan list 2 sama
#keduanya adalah objek bang berbeda
print("list 1 is list 2", list1 is list2)  #output False
print("list 1 is list 2", list1 is not list2) #output True
#ouput=True (objek yang berbeda)