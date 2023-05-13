# Author: Vip3rLi0n

import os
from sys import stdout
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style, Back, init
import time
colorama.init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')

def banners():
    stdout.write("                                                                                         \n")
    stdout.write(" "+Fore.LIGHTRED_EX +"██╗   ██╗██╗██████╗ ██████╗ ██████╗    ██╗     ██╗ ██████╗ ███╗   ██╗\n")
    stdout.write(" "+Fore.LIGHTRED_EX +"██║   ██║██║██╔══██╗╚════██╗██╔══██╗   ██║     ██║██╔═████╗████╗  ██║\n")
    stdout.write(" "+Fore.LIGHTRED_EX +"██║   ██║██║██████╔╝ █████╔╝██████╔╝   ██║     ██║██║██╔██║██╔██╗ ██║\n")
    stdout.write(" "+Fore.LIGHTRED_EX +"╚██╗ ██╔╝██║██╔═══╝  ╚═══██╗██╔══██╗   ██║     ██║████╔╝██║██║╚██╗██║\n")
    stdout.write(" "+Fore.LIGHTRED_EX +" ╚████╔╝ ██║██║     ██████╔╝██║  ██║   ███████╗██║╚██████╔╝██║ ╚████║\n")
    stdout.write(" "+Fore.LIGHTRED_EX +" ╚═══╝  ╚═╝╚═╝     ╚═════╝ ╚═╝  ╚═╝╚══════════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝\n")
    stdout.write(" "+Fore.YELLOW +"═════════════╦═════════════════════════════════╦═════════════════════\n")
    stdout.write(" "+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩════════════════════╗\n")
    stdout.write(" "+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"Author                "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"        Vip3r_Li0n                   "+Fore.YELLOW+"║\n")
    stdout.write(" "+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"Github                "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"        github.com/Vip3rLi0n         "+Fore.YELLOW+"║\n")
    stdout.write(" "+Fore.YELLOW   +"╚═══════════════════════════════════════════════════════════════════╝\n")
    print(f"{Fore.GREEN}                 Hacker Wars | Software Ranking Checker\n")
banners()

# Ask user to choose software type
option = input(f"{Fore.MAGENTA}[Meow!] - Choose the desired software type. (1-9)\n{Fore.RED}[ 1 ]  - {Fore.GREEN}Cracker\n{Fore.RED}[ 2 ]  - {Fore.GREEN}Hasher\n{Fore.RED}[ 3 ]  - {Fore.GREEN}Firewall\n{Fore.RED}[ 4 ]  - {Fore.GREEN}Hider\n{Fore.RED}[ 5 ]  - {Fore.GREEN}Seeker\n{Fore.RED}[ 6 ]  - {Fore.GREEN}SSH Exploit\n{Fore.RED}[ 7 ]  - {Fore.GREEN}FTP Exploit\n{Fore.RED}[ 8 ]  - {Fore.GREEN}DDoS Breaker\n{Fore.RED}[ 9 ]  - {Fore.GREEN}Virus Collector\n{Fore.RED}[ 10 ] - {Fore.GREEN}Nmap\n\n{Fore.CYAN}#Vip3rLi0n{Fore.BLUE}@{Fore.YELLOW}HWRankingChecker:- {Fore.MAGENTA}").strip()

# Ask user for PHPSESSID
phpsessid = input(f"\n{Fore.GREEN}[Meow!] - {Fore.YELLOW}Please enter your PHPSESSID!\n\n{Fore.CYAN}#Vip3rLi0n{Fore.BLUE}@{Fore.YELLOW}HWRankingChecker:- {Fore.MAGENTA}").strip()

# Define dictionary to map option number to software type
option_map = {
    '1': 'crc',
    '2': 'hash',
    '3': 'fwl',
    '4': 'hdr',
    '5': 'skr',
    '6': 'ssh',
    '7': 'ftp',
    '8': 'vbrk',
    '9': 'vcol',
    '10': 'nmap'
}

# Check if option is valid
if option not in option_map:
    print("Invalid option!")
else:
    # Set software type based on user's option
    software_type = option_map[option]
    url = f'https://hackerwars.io/ranking?show=software&orderby={software_type}'

cookies = {'PHPSESSID': phpsessid}

print(f"\n{Fore.GREEN}[Meow!] - {Fore.YELLOW}Please enter the number of minutes between each check.")
minutes = int(input(f"\n{Fore.CYAN}#Vip3rLi0n{Fore.BLUE}@{Fore.YELLOW}HWRankingChecker:- {Fore.MAGENTA}"))
wait_time = minutes * 60  # convert minutes to seconds

while True:
    response = requests.get(url, cookies=cookies)
    os.system('cls' if os.name == 'nt' else 'clear')

    if response.status_code == 200:
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')
        target_table = soup.find('table', {'class': 'table table-cozy table-bordered table-striped table-hover with-check'})
        if target_table:
            rows = target_table.find_all('tr')
            for row in rows[1:]:
                columns = row.find_all('td')
                rank = columns[0].get_text().strip()
                name = columns[1].get_text().strip()
                version = columns[2].get_text().strip()
                print(f"{Fore.GREEN}Rank: {Fore.MAGENTA}{rank}\n{Fore.GREEN}Name: {Fore.YELLOW}{name}\n{Fore.GREEN}Version: {Fore.RED}{version}\n{Fore.RESET}")
        else:
            print(f"{Fore.RED}\nTable not found on the page!{Fore.RESET}")
    else:
        print(f"\nError: {response.status_code}{Fore.RESET}")

    time.sleep(wait_time)