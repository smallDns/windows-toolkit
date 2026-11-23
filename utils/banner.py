from utils.color import AMARELO, RESET, AZUL_CELESTE, AZUL, LARANJA, BRANCO


def banner(version="1.0.0"):
  print(rf"""{AZUL_CELESTE}                                                   
                  ░██                  ░██                                         
                                       ░██                                         
░██    ░██    ░██ ░██░████████   ░████████  ░███████  ░██    ░██    ░██  ░███████  
░██    ░██    ░██ ░██░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██    ░██ ░██        
 ░██  ░████  ░██  ░██░██    ░██ ░██    ░██ ░██    ░██  ░██  ░████  ░██   ░███████  
  ░██░██ ░██░██   ░██░██    ░██ ░██   ░███ ░██    ░██   ░██░██ ░██░██          ░██ 
   ░███   ░███    ░██░██    ░██  ░█████░██  ░███████     ░███   ░███     ░███████  
{RESET}""")
  print(f"{AZUL}╔════════════════════════════════════════════════════════════╗{RESET}")
  print(
      f"{AZUL}║{RESET}  {BRANCO}Windows Toolkit{RESET}"
      f" {AMARELO}v{version:<10}{RESET} {AZUL}|{RESET}"
      f" {LARANJA}Python{RESET}                      {AZUL}║{RESET}"
  )
  print(f"{AZUL}╚════════════════════════════════════════════════════════════╝{RESET}")
