import subprocess
import platform

def ping(host):
    # '-n' for Windows, '-c' for Unix
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def main():
    file_name = 'domains.txt'
    try:
        with open(file_name, 'r') as file:
            domains = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"❌ File '{file_name}' not found.")
        return

    print("\n🌐 Pinging domains from file:\n")
    for domain in domains:
        if ping(domain):
            print(f"✅ {domain} is reachable.")
        else:
            print(f"❌ {domain} is NOT reachable.")

if __name__ == '__main__':
    main()
