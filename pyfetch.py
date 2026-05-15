import os, platform, psutil, datetime, time

def run(parent, args, terminal):
    try:
        boot_time = psutil.boot_time()
        uptime_seconds = int(time.time() - boot_time)
        uptime = str(datetime.timedelta(seconds=uptime_seconds))
        user = os.environ.get('USER') or "user"
        host = platform.node()
        mem = psutil.virtual_memory()
        
        logo = [
            "  ____        _   _                 ",
            " |  _ \ _   _| |_| |__   ___  _ __  ",
            " | |_) | | | | __| '_ \ / _ \| '_ \ ",
            " |  __/| |_| | |_| | | | (_) | | | |",
            " |_|    \__, |\__|_| |_|\___/|_| |_|",
            "        |___/                       "
        ]
        info = [
            f"{user}@{host}",
            "--------------------------",
            f"OS:      {platform.system()}",
            f"Kernel:  {platform.release()}",
            f"Uptime:  {uptime}",
            f"Shell:   PyOS 4.5.1",
            f"Memory:  {mem.used // 1048576}MB / {mem.total // 1048576}MB",
            f"Python:  {platform.python_version()}"
        ]
        terminal.insert("end", "\n")
        for i in range(max(len(logo), len(info))):
            l = logo[i] if i < len(logo) else " " * len(logo[0])
            r = info[i] if i < len(info) else ""
            terminal.insert("end", f" {l}   {r}\n")
        terminal.insert("end", "\n")
    except Exception as e:
        terminal.insert("end", f"Fetch Error: {e}\n")
