import nmap
import socket
import subprocess
import signal
import sys

# Ctrl + C Function
def signal_handler(sig, frame):
  print('[+] Finished Program.')
  sys.exit(0)
# SIGINT (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)
print('[+] Press Ctrl + C to end the program.')

# IP Verification Function
def ip_verification(ip):
  try:
    socket.inet_aton(ip)
    return True
  except socket.error:
    try:
      socket.getipbyname(ip)
      return True
    except socket.error:
      try:
        subprocess.check_output(["ping", "-c", "1", ip]) # Ping to IP
        return True
      except subprocess.CalledProcessError:
        return False

while True:
  try:   
    scan_name = input("[+] Scan Name: ");
    target_ip = input("[+] IP: ");
    print("[+] Total Ports (1-65535)")
    start_port = int(input("[+][+] Start Port: "));
    end_port = int(input("[+][+] End Port: "));
    # Ip and Ports Verification
    if ip_verification(target_ip) and (1 <= start_port <= end_port) and (1 <= end_port <= 65535) and (start_port <= end_port):
      print("[+] Valid IP and Ports");
    else:
      if not ip_verification(target_ip):
        print("[+] Invalid Ip")
      if not (1 <= start_port <= end_port and 1 <= end_port <= 65535):
        print("[+] Error: Ports (1-65535)");
      if start_port > end_port:
        print("[+] Error: Starting Port not greater than End Port.");
        continue;  
      else: 
        print("[+] Please enter valid numbers for ports!")
    break;  
  except KeyboardInterrupt:
    print("[+] Finished Program.")
    sys.exit(0)
    break;  

def scan_ports(target_ip, start_port, end_port):
  scanner = nmap.PortScanner()
  scanner.scaninfo = "-Pn -sV -sS -n --min-rate=5000"
  scan_result = scanner.scan(target_ip, f"{start_port}-{end_port}")
  scan_end = []
  for port in range(start_port, end_port + 1):
    if port in scanner[target_ip]['tcp'] and scanner[target_ip]['tcp'][port]['state'] == 'open':
      service_name = scanner[target_ip]['tcp'][port]['name']
      service_version = scanner[target_ip]['tcp'][port].get('version')
      scan = f"Port: {port} Service: {service_name} {service_version}"
      scan_end.append(scan)
  return scan_end

scan_result = scan_ports(target_ip, start_port, end_port)

for result in scan_result:
  print(result)

def save_scan(scan_end, scan_name):
  with open(f"./Scans/{scan_name}.txt", "w") as file:
    for result in scan_end:
      file.write(result + "\n")
  print(f"Scan results saved to Scans/{scan_name}.txt")

save_scan(scan_result, scan_name)

print("[+] END SCAN!")
