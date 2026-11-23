def format_bytes(value):
    value = float(value)
    for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
        if value < 1024 or unit == "PB":
            return f"{value:.2f} {unit}"
        value /= 1024

def percent_bar(percent, width=24):
    filled = int(width * float(percent) / 100)
    return f"[{'#' * filled}{'-' * (width - filled)}] {percent:.1f}%"

def heading(text):
    print("=" * 60)
    print(f"  {text}")
    print("=" * 60)
