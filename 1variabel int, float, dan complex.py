RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

#variabel int
print(RED + "\n--- VARIABEL INTEGER ---" )
int1 = int (20)
int2 = int (300)
int3 = int (-13 )
int4 = int (0o20 )
int5 = int (-0o103)
int6 = int (-0x212)
int7 = int (0x56)


print("Integer=",int1,int2,int3,int4,int5,int6,int7)


#variabel float
print(BLUE +"\n--- VARIABEL FLOAT ---")
float1 = float (0.1) 
float2 = float (1.20)
float3 = float (-41.2 )
float4 = float (32.23e123)
float5 = float (-92)
float6 = float (-32.52e10)
float7 = float (60.2e-13) 

print("Float=",float1,float2,float3,float4,float5,float6,float7)

#variabel complex
print(YELLOW +"\n--- VARIABEL COMPLEX ---")
complex1 = complex (3.14j)
complex2 = complex (35.j)
complex3 = complex (3.12e-12j)
complex4 = complex (873j)
complex5 = complex (-.123+0J)
complex6 = complex (3e+123J)
complex7 = complex (4.31e-4j)

print("Complex=",complex1,complex2,complex3,complex4,complex5,complex6,complex7)





