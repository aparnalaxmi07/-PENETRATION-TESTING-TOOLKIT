from modules.port_scanner import scan_ports
from modules.brute_forcer import ssh_brute_force

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. SSH Brute Forcer")
    choice = input("Select a module (1/2): ")

    if choice == '1':
        target = input("Enter target IP: ")
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
        open_ports = scan_ports(target, start_port, end_port)
        print(f"Open ports: {open_ports}")

    elif choice == '2':
        host = input("Enter target IP: ")
        username = input("Enter username: ")
        password_list = input("Enter path to password list: ").splitlines()
        ssh_brute_force(host, username, password_list)

if __name__ == "__main__":
    main()
