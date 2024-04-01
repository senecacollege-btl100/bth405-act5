# Concurrent Echo Server in Python

This repository contains a simple implementation of a concurrent echo server in Python, along with a corresponding client.

## Server (server.py)

The server listens for incoming connections from clients on localhost and a specified port. It utilizes threading to handle multiple client connections simultaneously. Upon receiving a message from a client, it echoes the message back to the client. The server can handle a special message "quit" to close the connection with the client while remaining running and able to accept new connections.

### How to Run the Server:

1. Open a terminal or command prompt.
2. Navigate to the directory where `server.py` is located.
3. Run the server script by typing:

4. You should see a message indicating that the server is listening on a specific host and port (e.g., `Server listening on localhost:65432`).

## Client (client.py)

The client connects to the server using TCP and prompts the user to enter messages to send to the server. It displays the server's response for each message sent. If the user types "quit", the client sends this message to the server, closes the socket, and exits the application.

### How to Run the Client:

1. Open another terminal or command prompt.
2. Navigate to the directory where `client.py` is located.
3. Run the client script by typing:
4. You should see a message indicating that the server is listening on a specific host and port (e.g., `Server listening on localhost:65432`).

## Client (client.py)

The client connects to the server using TCP and prompts the user to enter messages to send to the server. It displays the server's response for each message sent. If the user types "quit", the client sends this message to the server, closes the socket, and exits the application.

### How to Run the Client:

1. Open another terminal or command prompt.
2. Navigate to the directory where `client.py` is located.
3. Run the client script by typing:
