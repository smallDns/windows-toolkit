import os
import platform
import shutil
import socket
import subprocess
from utils.color import RESET,AMARELO,AZUL,AZUL_CELESTE,VERDE,VERMELHO,LARANJA
import psutil


def run_checks():
  results = []
  results.append((
      "Sistema",
      "Windows" if os.name == "nt" else platform.system(),
      os.name == "nt",
  ))
  disk = shutil.disk_usage(os.path.abspath(os.sep))
  results.append((
      "Espaco livre na unidade atual",
      f"{disk.free/(1024**3):.2f} GB",
      disk.free > 2 * 1024**3,
  ))
  ram = psutil.virtual_memory()
  results.append((
      "RAM disponivel",
      f"{ram.available/(1024**3):.2f} GB",
      ram.available > 512 * 1024**2,
  ))
  results.append(("CPU usage", f"{psutil.cpu_percent(interval=0.5)}%", True))
  try:
    socket.gethostbyname("www.microsoft.com")
    results.append(("DNS/Internet (resolucao)", "OK: www.microsoft.com", True))
  except OSError:
    results.append(
        ("DNS/Internet (resolucao)", "Falha na resolucao DNS", False)
    )
  if os.name == "nt":
    try:
      r = subprocess.run(
          ["ping", "-n", "1", "-w", "1500", "8.8.8.8"],
          capture_output=True,
          text=True,
          timeout=4,
      )
      results.append((
          "Ping para 8.8.8.8",
          "Resposta" if r.returncode == 0 else "Sem resposta",
          r.returncode == 0,
      ))
    except Exception:
      results.append(
          ("Ping para 8.8.8.8", "Nao foi possivel executar", False)
      )
  return results


def show():
  for name, detail, ok in run_checks():
    status = "[OK]" if ok else "[AVISO]"
    cor_status = VERDE if ok else VERMELHO
    cor_detail = AZUL_CELESTE if ok else AMARELO

    print(
        f"{cor_status}{status:<9}{RESET} {AZUL}{name:<32}{RESET}"
        f" {cor_detail}{detail}{RESET}"
    )

  print(
      f"\n{LARANJA}Diagnosticos simples. Resultados podem variar conforme"
      f" firewall/rede.{RESET}"
  )
