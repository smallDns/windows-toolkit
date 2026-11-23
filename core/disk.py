from utils.color import VERMELHO, VERDE, AMARELO, RESET, AZUL_CELESTE, AZUL, LARANJA, BRANCO
import psutil
from utils.formatter import format_bytes


def get_data():
  rows = []
  for p in psutil.disk_partitions(all=False):
    try:
      u = psutil.disk_usage(p.mountpoint)
      rows.append({
          "device": p.device,
          "mountpoint": p.mountpoint,
          "filesystem": p.fstype,
          "total": u.total,
          "used": u.used,
          "free": u.free,
          "percent": u.percent,
      })
    except (PermissionError, OSError):
      continue
  return rows


def show():
  rows = get_data()
  if not rows:
    print(f"{VERMELHO}Nenhuma unidade acessivel encontrada.{RESET}")
  for d in rows:
    uso = d["percent"]
    cor_uso = VERDE if uso < 70 else (AMARELO if uso < 90 else VERMELHO)

    print(
        f"\n{AZUL_CELESTE}{d['device']}{RESET}"
        f"  {LARANJA}[{d['filesystem']}]{RESET}"
    )
    print(f"  {AZUL}Montagem {BRANCO}:{RESET} {BRANCO}{d['mountpoint']}{RESET}")
    print(
        f"  {AZUL}Total    {BRANCO}:{RESET}"
        f" {BRANCO}{format_bytes(d['total'])}{RESET}"
    )
    print(
        f"  {AZUL}Usado    {BRANCO}:{RESET} {cor_uso}{format_bytes(d['used'])}"
        f" ({uso}%){RESET}"
    )
    print(
        f"  {AZUL}Livre    {BRANCO}:{RESET}"
        f" {VERDE}{format_bytes(d['free'])}{RESET}"
    )
