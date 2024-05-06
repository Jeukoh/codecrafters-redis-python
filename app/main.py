# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    PONG = "+PONG\r\n"
    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, addr = server_socket.accept() # wait for client
    
    with conn:
        data = conn.recv(1024)
        data = data.decode()
        # TODO
        # https://lethain.com/redis-protocol/
        conn.send(PONG.encode())

if __name__ == "__main__":
    main()
