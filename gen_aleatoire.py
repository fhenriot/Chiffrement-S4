import time
a = 999
b = 100000
m = 999999
nombre = time.time()

for i in range(0, 30):
	nombre = int((a * nombre + b) % m);
	print str(nombre) + " "