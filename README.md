# Port Scanner
This is a simple bash script that allows you to perform port scanning on a target IP address. It utilizes the `nmap` tool to scan for open ports within a specified range and saves the scan results to a file.

## Prerequisites
- Linux operating system.
- `nmap` tool installed (`sudo apt install nmap` or `brew install nmap`).

## Usage

1. Clone the repository and navigate to the script's directory:

```bash
git clone https://github.com/G3kSec/PortScanner-GNUBash/
```
```bash
cd port-scanner
```

2. Make the script executable:
```bash
chmod +x port_scanner.sh
```

3. Run the script
```bash
sudo ./port_scanner.sh
```
4. Follow the prompts to provide the necessary information:

- Enter a name for the scan.
- Enter the target IP address to scan.
- Specify the range of ports to scan (start and end ports).

5. The script will validate the IP address and port range. If the input is valid, the scanning process will begin.

6. Once the scan is complete, the script will display the open ports and their corresponding services.

7. The scan results will be saved to a file in the `Scans` directory with the format: `scan_name.txt`.

8. Press `Ctrl + C` to exit the script at any time.

## Considerations

- This script requires the nmap tool to be installed. Make sure you have it installed before running the script.
- The script validates the IP address and port range input to ensure they are within the correct format and range.
- The scanning process may take some time depending on the range of ports and the network speed.
- By default, the script uses the following nmap options:
  - `-Pn`: Treat all hosts as online (skip host discovery).
  - `-sV`: Probe open ports to determine service/version info.
  -  `-sS`: TCP SYN scanning (default scan type).
  -  `-n`: Disable DNS resolution.
  -  `--min-rate=5000`: Send packets at a rate of 5000 per second.
- The scan results will be saved in the Scans directory, and each scan will have its own separate file.
- It is recommended to use this script responsibly and with proper authorization. Unauthorized port scanning may violate the terms of service of your network provider or target system.

## Acknowledgments
This script utilizes the `nmap` tool, which is a powerful and versatile network scanning tool. Visit the official [nmap website](https://nmap.org/) for more information and documentation on how to use `nmap` effectively.

```
██████╗ ██╗   ██╗     ██████╗ ██████╗ ██╗  ██╗███████╗███████╗ ██████╗
██╔══██╗╚██╗ ██╔╝    ██╔════╝ ╚════██╗██║ ██╔╝██╔════╝██╔════╝██╔════╝
██████╔╝ ╚████╔╝     ██║  ███╗ █████╔╝█████╔╝ ███████╗█████╗  ██║     
██╔══██╗  ╚██╔╝      ██║   ██║ ╚═══██╗██╔═██╗ ╚════██║██╔══╝  ██║     
██████╔╝   ██║       ╚██████╔╝██████╔╝██║  ██╗███████║███████╗╚██████╗
╚═════╝    ╚═╝        ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝
```
