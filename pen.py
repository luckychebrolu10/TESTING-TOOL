import socket
import time

def port_scanner(target, start_port, end_port):
    print(f"\n[+] Scanning ports on {target} from {start_port} to {end_port}")
    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"[*] Port {port} is open")
            s.close()
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")

def brute_force_simulation(correct_password, wordlist_path):
    print("\n[+] Simulating brute-force attack...")
    try:
        with open(wordlist_path, 'r') as file:
            for line in file:
                password = line.strip()
                print(f"Trying: {password}")
                time.sleep(0.5)  # Slow down to simulate attack
                if password == correct_password:
                    print(f"[+] Password found: {password}")
                    return
        print("[-] No matching password found.")
    except FileNotFoundError:
        print("[!] Wordlist file not found.")

def main():
    while True:
        print("\n=== Simple Penetration Testing Toolkit ===")
        print("1. Port Scanner")
        print("2. Brute Force Simulation")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            target = input("Enter target IP: ")
            start_port = int(input("Start port: "))
            end_port = int(input("End port: "))
            port_scanner(target, start_port, end_port)

        elif choice == '2':
            correct_password = input("Set a correct password for simulation: ")
            wordlist_path = input("Enter path to wordlist file: ")
            brute_force_simulation(correct_password, wordlist_path)

        elif choice == '3':
            print("Exiting ...")
            break

        else:
            print("Invalid option.")

if _name_ == "_main_":
    main()
