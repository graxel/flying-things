import socket
import subprocess
import platform

def ping_host(ip):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)#[0]
    except socket.herror:
        hostname = None
    return hostname

def main():
    base_ip = "192.168.0."
    for i in range(1, 255):
        ip = base_ip + str(i)
        if ping_host(ip):
            hostname = get_hostname(ip)
            print(f"{ip} - {hostname if hostname else 'Hostname not found'}")

if __name__ == "__main__":
    main()
