import socket

def main():
    host = 'localhost'
    port = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Connected to server.")
        
        while True:
            message = input("Enter message to send (type 'quit' to exit): ")
            s.sendall(message.encode("utf-8"))
            if message == "quit":
                break
            data = s.recv(1024)
            print("Received from server:", data.decode("utf-8"))

if __name__ == "__main__":
    main()
