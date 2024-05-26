import socket
import psutil
from datetime import datetime

# Pfad zur Logdatei festlegen
log_file_path = 'offen_ports.txt'

def check_port(port, host):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        result = sock.connect_ex((host, port))
        return result == 0

def get_process_using_port(port):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            for conn in proc.info['connections']:
                if conn.laddr.port == port:
                    return proc.info
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return None

def log_and_print(message):
    print(message)
    with open(log_file_path, 'a') as f:
        f.write(message + '\n')
