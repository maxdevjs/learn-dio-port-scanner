# $ sudo pip3 install python-nmap
# $ sudo python3 pscan.py
import nmap

scanner = nmap.PortScanner()

print("Welcome to the mighty scanner")
print("<--------------------------->")

ip = input ("Enter IP: ")
print("Provided IP is: ", ip)
type(ip)

menu = input("""\nChoose the scan type
  1 -> SYN
  2 -> UDP 
  3 -> COMPREHENSIVE
  
Enter (1/2/3): """ )

print("Chosen option: ", menu)

if menu == "1":
  print("Nmap version: ", scanner.nmap_version())
  scanner.scan(ip, '1-1024', '-v -sS')
  print(scanner.scaninfo())
  print("IP status: ", scanner[ip].state())
  print(scanner[ip].all_protocols())
  print(" ")
  print("Open ports: ", scanner[ip]['tcp'].keys())
elif menu == "2":
  print("Nmap version: ", scanner.nmap_version())
  scanner.scan(ip, '1-1024', '-v -sU')
  print(scanner.scaninfo())
  print("IP status: ", scanner[ip].state())
  print(scanner[ip].all_protocols())
  print(" ")
  print("Open ports: ", scanner[ip]['udp'].keys())
elif menu == "3":
  print("Nmap version: ", scanner.nmap_version())
  scanner.scan(ip, '1-1024', '-v -sC')
  print(scanner.scaninfo())
  print("IP status: ", scanner[ip].state())
  print(scanner[ip].all_protocols())
  print(" ")
  print("Open ports: ", scanner[ip]['tcp'].keys())
else:
  print ("Wrong choise")

