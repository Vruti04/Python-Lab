#Convert Bytes into KB,MB,GB
a=int(input("Enter Bytes:"))
#KB
KB=a/1000
print("KB:",KB)
#MB
MB=a*10**-6
print("MB:",MB)
#GB
GB=a*10**-9
print("GB:",GB)
