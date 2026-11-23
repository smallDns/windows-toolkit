from utils.color import VERDE, AMARELO, BRANCO, VERMELHO, AZUL, RESET, LARANJA
import psutil
from utils.formatter import format_bytes, percent_bar


def get_data():
  v = psutil.virtual_memory()
  s = psutil.swap_memory()
  return {
      "total": v.total,
      "used": v.used,
      "available": v.available,
      "percent": v.percent,
      "swap_total": s.total,
      "swap_used": s.used,
      "swap_percent": s.percent,
  }


def show():
  d = get_data()

  # Cores dinâmicas para RAM e Swap
  cor_ram = (
      VERDE if d["percent"] < 60 else (AMARELO if d["percent"] < 85 else VERMELHO)
  )
  cor_swap = (
      VERDE
      if d["swap_percent"] < 60
      else (AMARELO if d["swap_percent"] < 85 else VERMELHO)
  )

  print(
      f"{AZUL}RAM total       {BRANCO}:{RESET}"
      f" {BRANCO}{format_bytes(d['total'])}{RESET}"
  )
  print(
      f"{AZUL}RAM utilizada   {BRANCO}:{RESET}"
      f" {cor_ram}{format_bytes(d['used'])} ({d['percent']}%){RESET}"
  )
  print(
      f"{AZUL}RAM disponivel  {BRANCO}:{RESET}"
      f" {VERDE}{format_bytes(d['available'])}{RESET}"
  )
  print(
      f"{AZUL}Uso             {BRANCO}:{RESET}"
      f" {cor_ram}{percent_bar(d['percent'])}{RESET}"
  )
  print(
      f"\n{LARANJA}Memoria virtual {BRANCO}:{RESET}"
      f" {cor_swap}{format_bytes(d['swap_used'])}{RESET} {BRANCO}/{RESET}"
      f" {BRANCO}{format_bytes(d['swap_total'])}{RESET}"
      f" {cor_swap}({d['swap_percent']}%){RESET}"
  )
