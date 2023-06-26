import scapy.all as s

def scan(ip):
    s.wireshark(ip)

scan(open('wpahack-01.cap'))
