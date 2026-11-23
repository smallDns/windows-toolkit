from datetime import datetime
import json
from pathlib import Path
from utils.color import RESET,AMARELO,AZUL,AZUL_CELESTE,VERDE,BRANCO,LARANJA
from core import cpu, diagnostics, disk, hardware, memory, network, processes, system

REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"


def collect():
  return {
      "generated_at": datetime.now().isoformat(timespec="seconds"),
      "system": system.get_data(),
      "cpu": cpu.get_data(),
      "memory": memory.get_data(),
      "disks": disk.get_data(),
      "network": network.get_data(),
      "processes": processes.get_data(limit=25),
      "hardware": hardware.get_data(),
      "diagnostics": [
          {"name": n, "detail": d, "ok": ok}
          for n, d, ok in diagnostics.run_checks()
      ],
  }


def generate():
  print(f"{AMARELO}Coletando dados do sistema e gerando relatorios...{RESET}")
  REPORT_DIR.mkdir(exist_ok=True)
  data = collect()
  stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  json_path = REPORT_DIR / f"system_report_{stamp}.json"
  txt_path = REPORT_DIR / f"system_report_{stamp}.txt"
  json_path.write_text(
      json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
  )

  lines = [
      "WINDOWS TOOLKIT - SYSTEM REPORT",
      f"Generated: {data['generated_at']}",
      "=" * 55,
  ]
  for section, values in data.items():
    lines.append(f"\n[{section.upper()}]")
    if isinstance(values, dict):
      lines.extend(f"{k}: {v}" for k, v in values.items())
    elif isinstance(values, list):
      for item in values:
        lines.append(str(item))
    else:
      lines.append(str(values))

  txt_path.write_text("\n".join(lines), encoding="utf-8")

  print(f"\n{VERDE}Relatorios gerados com sucesso:{RESET}")
  print(f"  {AZUL}TXT {BRANCO}:{RESET} {AZUL_CELESTE}{txt_path}{RESET}")
  print(f"  {AZUL}JSON{BRANCO}:{RESET} {LARANJA}{json_path}{RESET}")
