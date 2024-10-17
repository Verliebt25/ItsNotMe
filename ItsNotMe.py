import subprocess
import time

# Lista de IPs a las que cambiar
ip_addresses = [
    "192.168.1.100",
    "192.168.1.101",
    "192.168.1.102"
]

# Interfaz de red que deseas cambiar (ajústalo según tu configuración)
interface = "ens160"

def change_ip(ip, interface):
    try:
        # Comando para cambiar la IP
        subprocess.run(["sudo", "ifconfig", interface, ip, "netmask", "255.255.255.0"], check=True)
        print(f"IP cambiada a: {ip}")
    except subprocess.CalledProcessError as e:
        print(f"Error al cambiar la IP: {e}")

def main():
    while True:
        for ip in ip_addresses:
            change_ip(ip, interface)
            time.sleep(5)  # Espera los segundos indicados

if __name__ == "__main__":
    main()
