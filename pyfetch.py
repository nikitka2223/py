import os
import platform
import psutil
import datetime

def run(parent, args, terminal):
    # Данные системы
    user = os.getlogin() if hasattr(os, 'getlogin') else "user"
    host = platform.node()
    os_name = "Void Linux" # Раз мы на Void
    kernel = platform.release()
    uptime = str(datetime.timedelta(seconds=int(psutil.boot_time())))
    shell = "PyOS 4.5.1"
    
    # Расчет памяти
    mem = psutil.virtual_memory()
    mem_used = mem.used // (1024 ** 2)
    mem_total = mem.total // (1024 ** 2)
    
    # ASCII Логотип (Змейка)
    logo = [
        "  ____        _   _                 ",
        " |  _ \ _   _| |_| |__   ___  _ __  ",
        " | |_) | | | | __| '_ \ / _ \| '_ \ ",
        " |  __/| |_| | |_| | | | (_) | | | |",
        " |_|    \__, |\__|_| |_|\___/|_| |_|",
        "        |___/                       "
    ]
    
    # Инфо-блок
    info = [
        f"{user}@{host}",
        "--------------------------",
        f"OS:      {os_name}",
        f"Kernel:  {kernel}",
        f"Uptime:  {uptime}",
        f"Shell:   {shell}",
        f"Memory:  {mem_used}MB / {mem_total}MB",
        f"Python:  {platform.python_version()}"
    ]

    # Вывод в терминал
    terminal.insert("end", "\n")
    max_lines = max(len(logo), len(info))
    
    for i in range(max_lines):
        l_part = logo[i] if i < len(logo) else " " * len(logo[0])
        r_part = info[i] if i < len(info) else ""
        terminal.insert("end", f" {l_part}   {r_part}\n")
    
    terminal.insert("end", "\n")
    terminal.see("end")