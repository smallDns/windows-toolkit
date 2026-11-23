import datetime
import platform
import socket
from utils.color import RESET, AMARELO, AZUL, AZUL_CELESTE, VERDE, LARANJA, BRANCO
import psutil


def get_data():
  return {
      "hostname": socket.gethostname(),
      "username": __import__("getpass").getuser(),
      "system": platform.system(),
      "windows_release": platform.release(),
      "version": platform.version(),
      "architecture": platform.machine(),
      "python": platform.python_version(),
      "boot_time": datetime.datetime.fromtimestamp(psutil.boot_time()).strftime(
          "%Y-%m-%d %H:%M:%S"
      ),
  }


def show():
  data = get_data()
  cores_valores = {
      "hostname": AZUL_CELESTE,
      "username": VERDE,
      "python": LARANJA,
      "boot_time": AMARELO,
  }

  for key, value in data.items():
    label = key.replace("_", " ").title()
    cor_val = cores_valores.get(key, BRANCO)
    print(f"{AZUL}{label:<22}{BRANCO}:{RESET} {cor_val}{value}{RESET}")
