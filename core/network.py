import socket
from utils.color import RESET,AMARELO,AZUL,AZUL_CELESTE,VERDE,VERMELHO,LARANJA,BRANCO,ROXO
import psutil


def get_data():
  adapters = []
  stats = psutil.net_io_counters()
  for name, addresses in psutil.net_if_addrs().items():
    ips = []
    for a in addresses:
      if a.family in (socket.AF_INET, socket.AF_INET6):
        ips.append({
            "family": "IPv4" if a.family == socket.AF_INET else "IPv6",
            "address": a.address,
        })
    adapters.append({
        "name": name,
        "addresses": ips,
        "is_up": (
            psutil.net_if_stats().get(name).isup
            if name in psutil.net_if_stats()
            else None
        ),
    })
  return {
      "adapters": adapters,
      "bytes_sent": stats.bytes_sent,
      "bytes_received": stats.bytes_recv,
      "packets_sent": stats.packets_sent,
      "packets_received": stats.packets_recv,
  }


def show():
  d = get_data()
  print(f"{AMARELO}Adaptadores:{RESET}")
  for a in d["adapters"]:
    status = "Ativo" if a["is_up"] else "Desativado"
    cor_status = VERDE if a["is_up"] else VERMELHO

    print(
        f"\n {AZUL}-{RESET} {AZUL_CELESTE}{a['name']}{RESET}"
        f" ({cor_status}{status}{RESET})"
    )
    for ip in a["addresses"]:
      cor_fam = LARANJA if ip["family"] == "IPv4" else ROXO
      print(
          f"    {cor_fam}{ip['family']}{BRANCO}:{RESET}"
          f" {BRANCO}{ip['address']}{RESET}"
      )

  print(
      f"\n{AZUL}Bytes enviados   {BRANCO}:{RESET}"
      f" {VERDE}{d['bytes_sent']:,}{RESET}"
  )
  print(
      f"{AZUL}Bytes recebidos  {BRANCO}:{RESET}"
      f" {AZUL_CELESTE}{d['bytes_received']:,}{RESET}"
  )
  print(
      f"{AZUL}Pacotes enviados {BRANCO}:{RESET}"
      f" {LARANJA}{d['packets_sent']:,}{RESET}"
  )
  print(
      f"{AZUL}Pacotes recebidos{BRANCO}:{RESET}"
      f" {AMARELO}{d['packets_received']:,}{RESET}"
  )
