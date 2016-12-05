#Using socket for low level network interfacing

import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("128.238.66.83",8888))
sock.settimeout(200)
string = sock.recv(2048)
print (string)
while True:
	rec = sock.recv(1024)
	while rec == "\n":
		rec = sock.recv(1024)	
	if(rec.startswith("Convert")):
		num = rec.find("(",0,len(rec))
		sec = rec.find(")")
		fac1 = rec.rfind("(",0,len(rec))
		fac2 = rec.rfind(")",0,len(rec))

		num = int(rec[(num+1):sec])
		base = int(rec[(fac1+1):fac2])

		print (rec)

		if base == 10:
			sock.send(str(num)+"\n")
			print (num,"is",num, "in decimal")

		if base == 16:
			sock.send(hex(num)+"\n")
			print (num,"is",hex(num),"in hex")

		if base == 2:
			sock.send(bin(num)+"\n")
			print (num,"is",bin(num), "in binary")
	if rec.startswith("Phase"):
		break

print (rec) #Phase 3

while not rec.startswith("How"):
	rec = sock.recv(1024)
	break

print (rec) #How do you spell
sock.send("Salsaman\n")
print("Salsaman")
rec = sock.recv(1024) 
print(rec)
rec = sock.recv(1024)
print (rec)
print (rec)
