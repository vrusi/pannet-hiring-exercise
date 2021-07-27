import socket
import sys
import ipaddress

def scan_tcp(host, port):
    location = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try: 
        result = sock.connect_ex(location)
        if (result == 0):
            print(str(port) + '/tcp open')
    except Exception:
        pass

    sock.close()

    return result == 0


def scan_udp(host, port):
    location = (host, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.sendto(b"", location)
        """ no error means port is probably open """
        print(str(port) + '/udp may be open')

    except Exception: 
        pass

    sock.close()


def scan_network(host, should_scan_udp):
    for port in range(0, 65535):
        if (scan_tcp(host, port) != True and should_scan_udp):
            scan_udp(host, port)


if __name__ == '__main__':

    print('Usage: python scanner.py [host_range_start] [host_range_end] [should_scan_udp (0 | 1)]\n')

    target_start = sys.argv[1]
    host_start = socket.gethostbyname(target_start) 
    
    target_end = ''
    host_end = ''
    
    should_scan_udp = False
    args_len = len(sys.argv)
    if (args_len == 2):
        print('Started scanning ports on: ' + host_start)

    if (args_len > 2):
        if (sys.argv[2] == 0 or sys.argv[2] == 1):
            should_scan_udp = bool(int(sys.argv[3]))
        else:
            target_end = sys.argv[2]
            host_end = socket.gethostbyname(target_end) 
            print('Started scanning ports in range: ' + host_start + ' - ' + host_end)

    if (args_len > 3):
        should_scan_udp = bool(int(sys.argv[3]))
        
    if (host_end != ''):
        ip_start = ipaddress.IPv4Address(host_start)
        ip_end = ipaddress.IPv4Address(host_end)
        for ip_int in range(int(ip_start), int(ip_end) + 1):
            host = str(ipaddress.IPv4Address(ip_int))
            print('\nScanning ' + host)
            scan_network(host, should_scan_udp)
            print('Done')
    else: 
        scan_network(host_start, should_scan_udp)
        print('Done')
