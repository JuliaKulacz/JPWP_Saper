import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("127.0.0.1", 50000)

print('Client 2 has started connection!')

s.connect(address)

while True:
    print("Your message:")
    msg = input()
    data = s.sendall(str.encode(msg))
    resp = s.recv(2048)
    print("Client 1:", resp.decode())