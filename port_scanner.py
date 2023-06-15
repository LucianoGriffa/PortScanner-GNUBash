import nmap
import socket
import subprocess

def host_verification(host):
  try:
    socket.inet_aton(host)
    return True
  except socket.error:
    try:
      socket.gethostbyname(host)
      return True
    except socket.error:
      return False

while True:
  try:
    scan_name = input("[+] Scan Name: ")
    target_host = input("[+] Host: ")
    start_port = int(input("[+] Start Port: "))
    end_port = int(input("[+] End Port: "))
    # Verificación de los puertos
    if not (1 <= start_port <= end_port and 1 <= end_port <= 65535):
      print("Error: Ports (1-65535)")
      continue
    if start_port > end_port:
      print("Error: Starting Port not greater than End Port.")
      continue
    # Verificación del host    
    if host_verification(target_host):
      print("Valid Host")
    else:
      print("Invalid Host")
    break;
  except:
    print("[+] Please enter valid numbers for ports!")

def scan_ports(target_host, start_port, end_port):
  scanner = nmap.PortScanner()
  scanner.scaninfo = "-Pn -sV -sS -p- -n --min-rate=5000"
  scan_result = scanner.scan(target_host, f"{start_port}-{end_port}")
  for port in range(start_port, end_port + 1):
    if scanner[target_host]['tcp'][port]['state'] == 'open':
      service_name = scanner[target_host]['tcp'][port]['name']
      service_version = scanner[target_host]['tcp'][port]['version']
      scan = f"Port {port} ({service_name}): {service_version}"
      scan_end = []
      scan_end.append(scan)

scan_ports(target_host, start_port, end_port)

def save_scan(scan_end):
  command = f"echo '{scan}' > {scan_name}.txt && ls -l"
  subprocess.run(command, shell=True, capture_output=False, text=True)

print("[+] END SCAN!")