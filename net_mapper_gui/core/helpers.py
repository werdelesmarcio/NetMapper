import socket

def get_service_name(port, protocol):
    try:
        return socket.getservbyport(port, protocol)
    except OSError:
        return "Unknown Service"

def grab_banner(target, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
            banner = s.recv(1024).decode().strip()
            return banner.split()[0] if banner else "Unknown Service"
    except (socket.timeout, socket.error):
        return "No banner available"
