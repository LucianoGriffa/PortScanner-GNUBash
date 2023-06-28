#!/bin/bash

function signal_handler() {
  echo "[*] Finished Program."
  exit 0
}

trap signal_handler SIGINT

echo "[*] Press Ctrl + C to end the program."

function ip_verification() {
  ip=$1
  if ping -c 1 "$ip" >/dev/null 2>&1; then
    return 0
  else
    return 1
  fi
}

while true; do
  read -p "[*] Scan Name: " scan_name
  read -p "[*] IP: " target_ip
  echo "[*] Total Ports (1-65535)"
  read -p "[*][*] Start Port: " start_port
  read -p "[*][*] End Port: " end_port
  # IP and Ports Verification
  if ip_verification "$target_ip" && ((start_port >= 1 && start_port <= end_port && end_port <= 65535)); then
    echo "[*] Valid IP and Ports"
    break
  else
    if ! ip_verification "$target_ip"; then
      echo "[*] Invalid IP"
    fi
    if ! ((start_port >= 1 && start_port <= end_port && end_port <= 65535)); then
      echo "[*] Error: Ports (1-65535)"
    fi
    if ((start_port > end_port)); then
      echo "[*] Error: Starting Port not greater than End Port."
    else
      echo "[*] Please enter valid numbers for ports!"
    fi
  fi
done

function scan_ports() {
  target_ip=$1
  start_port=$2
  end_port=$3
  scan_result=$(nmap -Pn -sV -sS -n --min-rate=5000 -p "$start_port-$end_port" "$target_ip" | awk '/open/{print "Port: " $1 " Service: " $2 " " $3}')
  echo "$scan_result"
}

scan_result=$(scan_ports "$target_ip" "$start_port" "$end_port")
echo "$scan_result"

function save_scan() {
  scan_end=$1
  scan_name=$2
  echo "$scan_end" >"./Scans/$scan_name.txt"
  echo "Scan results saved to Scans/$scan_name.txt"
}

save_scan "$scan_result" "$scan_name"

echo "[*] END SCAN!"
