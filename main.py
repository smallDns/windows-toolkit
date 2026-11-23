import os
import sys
from pathlib import Path

try:
    import psutil
except ImportError:
    int("Dependencia psutil nao instalada.")
    print("Execute: py -m pip install -r requirements.txt")
    input("Pressione ENTER para sair...")
    sys.exit(1)

from core import system, cpu, memory, disk, network, processes, hardware, diagnostics, report
from utils.banner import banner
from utils.formatter import heading, format_bytes, percent_bar
from utils.color import AMARELO, AZUL, BRANCO, LARANJA, RESET, VERDE, VERMELHO

VERSION = "1.0.0"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPressione ENTER para continuar...")

def show(title, callback):
    clear()
    heading(title)
    callback()
    pause()

def main():
    while True:
        clear()
        banner(VERSION)
        print(f"  {AZUL}[01]{RESET} {BRANCO}System Information{RESET}")
        print(f"  {AZUL}[02]{RESET} {BRANCO}CPU Monitor{RESET}")
        print(f"  {AZUL}[03]{RESET} {BRANCO}RAM Monitor{RESET}")
        print(f"  {AZUL}[04]{RESET} {BRANCO}Disk Information{RESET}")
        print(f"  {AZUL}[05]{RESET} {BRANCO}Network Information{RESET}")
        print(f"  {LARANJA}[06]{RESET} {BRANCO}Process Manager{RESET}")
        print(f"  {LARANJA}[07]{RESET} {BRANCO}Hardware Information{RESET}")
        print(f"  {AMARELO}[08]{RESET} {BRANCO}System Diagnostics{RESET}")
        print(f"  {VERDE}[09]{RESET} {BRANCO}Generate System Report{RESET}")
        print(f"  {VERMELHO}[00]{RESET} {VERMELHO}Exit{RESET}")
        choice = input("\n  Select an option: ").strip()

        actions = {
            "1": ("System Information", system.show),
            "01": ("System Information", system.show),
            "2": ("CPU Monitor", cpu.show),
            "02": ("CPU Monitor", cpu.show),
            "3": ("RAM Monitor", memory.show),
            "03": ("RAM Monitor", memory.show),
            "4": ("Disk Information", disk.show),
            "04": ("Disk Information", disk.show),
            "5": ("Network Information", network.show),
            "05": ("Network Information", network.show),
            "6": ("Process Manager", processes.show),
            "06": ("Process Manager", processes.show),
            "7": ("Hardware Information", hardware.show),
            "07": ("Hardware Information", hardware.show),
            "8": ("System Diagnostics", diagnostics.show),
            "08": ("System Diagnostics", diagnostics.show),
            "9": ("Generate System Report", report.generate),
            "09": ("Generate System Report", report.generate),
        }
        if choice in ("0", "00"):
            print("\nSaindo do Windows Toolkit...")
            break
        if choice in actions:
            title, callback = actions[choice]
            show(title, callback)
        else:
            print("\nOpcao invalida.")
            pause()

if __name__ == "__main__":
    main()
