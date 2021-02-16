import socket
import sys
import threading
import logging

l = logging.getLogger("sockets")
h = logging.StreamHandler()
f = logging.Formatter("%(asctime)s: %(message)s")
h.setFormatter(f)
l.addHandler(h)
l.setLevel(logging.INFO)


def server(listen_on_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        l.critical("Error creating socket server")
        sys.exit(1)
    sock.bind(("0.0.0.0", listen_on_port))
    sock.listen(1)
    l.info("Socket server is up")
    connection, _ = sock.accept()
    for _ in range(3):
        data = connection.recv(1024)  # 1024 is max. buffer length
        connection.sendall(f"Server: {data.decode()}".encode())
    connection.close()
    l.info("Closing socket server")
    sock.close()


def client(send_to_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        l.critical("Error creating socket server")
        sys.exit(1)
    l.info("Client is active")
    sock.connect(("localhost", send_to_port))
    for _ in range(3):
        sock.sendall(input("Message: ").encode())
        print(sock.recv(1024).decode())
    sock.close()
    l.info("Closing client")


if __name__ == "__main__":
    port = 8081
    srv = threading.Thread(target=server, args=(port,))
    srv.start()
    client(port)
    srv.join()
