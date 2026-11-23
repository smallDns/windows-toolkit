import platform
import psutil
import time
from utils.color import AMARELO, RESET, AZUL_CELESTE, AZUL, LARANJA, BRANCO

def get_data():
    freq = psutil.cpu_freq()
    return {
        "model": platform.processor() or "Indisponivel",
        "physical_cores": psutil.cpu_count(logical=False) or "N/A",
        "logical_cores": psutil.cpu_count(logical=True) or "N/A",
        "usage_percent": psutil.cpu_percent(interval=1),
        "frequency_mhz": round(freq.current, 1) if freq else None,
    }

def show():
    data = get_data()
    print(f"    {AZUL}Modelo            {BRANCO}:{RESET} {BRANCO}{data['model']}{RESET}")
    print(f"    {AZUL}Nucleos fisicos   {BRANCO}:{RESET} {AZUL_CELESTE}{data['physical_cores']}{RESET}")
    print(f"    {AZUL}Nucleos logicos   {BRANCO}:{RESET} {AZUL_CELESTE}{data['logical_cores']}{RESET}")
    print(f"    {AZUL}Uso atual         {BRANCO}:{RESET} {data['usage_percent']}%")
    print(f"    {AZUL}Frequencia        {BRANCO}:{RESET} {LARANJA}{data['frequency_mhz'] or 'N/A'} MHz{RESET}")
