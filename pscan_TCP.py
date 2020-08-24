import socket

# UDP: VoIP, video stremaing, ...
# open port <- UDP scanner
# open port -> UDP responde scanner

# close port <- UDP scanner
# close port -> ICMP 3 error scanner
# $ sudo nmap -v -sU localhost

# SYN (stealth), less noisy because of type of TCP request (not complete request)
# open port <- SYN scanner
# open port -> SYN / ACK scanner
# open port <- RST scanner

# close port <- SYN scanner
# close port -> RST scanner

# $ sudo nmap -v -sS localhost

#python3 pscan_TCP.py
# TCP (noisy), easy to detect

# ack = open
# open port <- syn scanner
# open port -> syn / ack scanner
# open port <- ack scanner

# reset = closed
# close port <- syn scanner
# close port -> rst scanner

# $ sudo nmap -v -sT localhost

# comprehensive
# $ sudo nmap -v -sC localhost

IP = "google.com"

ip = input("Enter HOST or IP to scan: ")
ports = []
portsNumber = int(input("Enter how many ports to scan: "))
# implement range

count = 0

while count < portsNumber:
  ports.append(int(input ("Enter PORT to scan: ")))
  count += 1

for port in ports:
  # IPV4 , TCP/IP
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.settimeout(0.05)
  # receives code of TCP transaction
  code = client.connect_ex((ip, port))

  # https://gist.github.com/gabrielfalcao/4216897

  if code == 0:
    print("Open port -> ", str(code))
  else:
    print("Closed port -> " + str(code))

print ("End scan")
