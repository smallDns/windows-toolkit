import platform
import subprocess
from utils.color import LARANJA,BRANCO,AZUL,AMARELO,AZUL_CELESTE,VERDE,VERMELHO,RESET
import psutil


def _powershell(query):
  try:
    cmd = ["powershell", "-NoProfile", "-Command", query]
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=12,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode == 0:
      return result.stdout.strip() or "Informacao indisponivel"
    return "Consulta nao disponivel"
  except Exception:
    return "PowerShell nao disponivel"


def get_data():
  info = {
      "CPU": platform.processor() or "Indisponivel",
      "RAM instalada": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
      "Placa-mae": _powershell(
          "(Get-CimInstance Win32_BaseBoard | Select-Object -First 1"
          " -ExpandProperty Product)"
      ),
      "Fabricante da placa-mae": _powershell(
          "(Get-CimInstance Win32_BaseBoard | Select-Object -First 1"
          " -ExpandProperty Manufacturer)"
      ),
      "BIOS": _powershell(
          "(Get-CimInstance Win32_BIOS | Select-Object -First 1"
          " -ExpandProperty SMBIOSBIOSVersion)"
      ),
      "GPU": _powershell(
          "(Get-CimInstance Win32_VideoController | Select-Object"
          " -ExpandProperty Name)"
      ),
      "Discos fisicos": _powershell(
          "(Get-PhysicalDisk | Select-Object FriendlyName, MediaType, Size |"
          " Format-Table -AutoSize | Out-String)"
      ),
  }
  return info


def show():
  cores_hardware = {
      "CPU": AZUL_CELESTE,
      "RAM instalada": VERDE,
      "GPU": LARANJA,
      "BIOS": AMARELO,
  }

  for label, value in get_data().items():
    if "indisponivel" in value.lower() or "nao disponivel" in value.lower():
      cor_val = VERMELHO
    else:
      cor_val = cores_hardware.get(label, BRANCO)

    if label == "Discos fisicos":
      print(f"\n{AZUL}{label:<25}{BRANCO}:{RESET}\n{AZUL_CELESTE}{value}{RESET}")
    else:
      print(f"{AZUL}{label:<25}{BRANCO}:{RESET} {cor_val}{value}{RESET}")
