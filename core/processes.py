from utils.color import BRANCO,RESET,AMARELO,AZUL,AZUL_CELESTE,VERDE,VERMELHO,LARANJA
import psutil


def get_data(limit=25):
  items = []
  for p in psutil.process_iter(["pid", "name", "username", "memory_info"]):
    try:
      info = p.info
      mem = info.get("memory_info")
      items.append({
          "pid": info["pid"],
          "name": info.get("name") or "?",
          "username": info.get("username") or "?",
          "memory": mem.rss if mem else 0,
      })
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      continue
  items.sort(key=lambda x: x["memory"], reverse=True)
  return items[:limit]


def show():
  print(f"{AZUL}{'PID':>7}  {'RAM (MB)':>10}  {'Processo'}{RESET}")
  print(f"{AZUL}{'-' * 48}{RESET}")

  for p in get_data():
    ram_mb = p["memory"] / 1024 / 1024
    # Cor dinâmica de acordo com o consumo de RAM do processo
    cor_ram = (
        VERMELHO if ram_mb >= 500 else (AMARELO if ram_mb >= 150 else VERDE)
    )

    print(
        f"{AZUL_CELESTE}{p['pid']:>7}{RESET} "
        f" {cor_ram}{ram_mb:>10.1f}{RESET}  {BRANCO}{p['name'][:32]}{RESET}"
    )

  print(
      f"\n{LARANJA}Lista ordenada por consumo de RAM. Consulta somente; nao"
      f" encerra processos.{RESET}"
  )
