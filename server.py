import socket
import threading

# Function to handle client connections
def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        message = data.decode("utf-8")
        print(f"Received from {addr}: {message}")
        if message == "quit":
            break
        conn.sendall(data)
    print(f"Connection closed by {addr}")
    conn.close()

# Main server function
def main():
    host = 'localhost'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    main()
