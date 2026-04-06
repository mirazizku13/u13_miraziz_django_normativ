import socket

HOST = "127.0.0.1"
PORT = 8080

def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST,PORT))
    sock.listen(5)

    print(f"Server running on http://{HOST}:{PORT}")

    while True:
        client_socket, addr = sock.accept()
        print(f"Yangi mijoz ulandi: {addr}")

        request = client_socket.recv(4096)


        try:
            text = request.decode("utf-8", errors="ignore")
            line = text.split("\r\n",1)[0]
            methos, path, _ = line.split(" ")
        except Exception:
            body = "<h1>404 not found</h1>"
            response = (
                ""
            )
        if method == "GET" and path == "/":
            pass