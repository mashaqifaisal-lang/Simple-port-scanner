import socket

def port_scanner(ip):
    print("Starting scan...")
    print("Target IP:", ip)
    print("-----------------------")

    ports = [21, 22, 23, 25, 80, 443]

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((ip, port))

        if result == 0:
            print("Port", port, "is OPEN")
        else:
            print("Port", port, "is closed")

        s.close()

ip_address = input("Enter IP address to scan: ")
port_scanner(ip_address)
