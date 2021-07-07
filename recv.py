import socket

protocol = socket.SOCK_DGRAM
add = socket.AF_INET

s = socket.socket(add,protocol)
ip=""
port=5658
s.bind((ip,port))

while True:
    x = s.recvfrom(1024)
    file = open("../html/try.txt","w")
    print(x[0].decode())
    file.write(x[0].decode())
    file.close()