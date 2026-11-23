# Windows Toolkit

A Python command-line toolkit for Windows system monitoring, diagnostics and administration.

## Features

- Windows version, architecture, hostname and boot time
- CPU model, core count, usage and frequency
- RAM and swap usage
- Disk partitions and space usage
- Network adapters, IP addresses and traffic counters
- Running process list (read-only)
- Hardware details (best-effort PowerShell queries)
- Basic diagnostics
- Export reports to TXT and JSON

## Requirements

- Windows 10 or Windows 11
- Python 3.10+
- `psutil`

## Installation (CMD or PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py main.py
```

You can also run without activating the environment:

```powershell
py -m pip install -r requirements.txt
py main.py
```

## Reports

Generated reports are saved to the `reports` directory. TXT and JSON files are created with timestamps.

## Project structure

```text
windows-toolkit/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── core/
│   ├── system.py
│   ├── cpu.py
│   ├── memory.py
│   ├── disk.py
│   ├── network.py
│   ├── processes.py
│   ├── hardware.py
│   ├── diagnostics.py
│   └── report.py
├── utils/
│   ├── banner.py
│   └── formatter.py
├── reports/
└── screenshots/
```

## Notes

The tool is primarily informational and does not require administrator privileges for basic features. Some Windows hardware/process details may be unavailable due to permissions. The process manager is read-only in this release.

## License

MIT.
