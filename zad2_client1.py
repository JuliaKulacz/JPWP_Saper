import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("127.0.0.1", 50000)

print('Client 1 has started connection!')
print('Waiting for client2...')

s.bind(address)

s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(2048)
    print("Client 2:", data.decode())
    print("Your message:")
    msg = input()
    conn.sendall(str.encode(msg))
