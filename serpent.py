import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def run(parent, args, terminal):
    NAME = "Serpent Browser v1.2"
    
    if not args:
        terminal.insert("end", f"{NAME}\n" + "="*30 + "\n")
        terminal.insert("end", "Usage:\n serpent <url>\n serpent -s <query>\n serpent -save <url> <file>\n")
        return

    cmd = args[0]
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; VoidLinux; x86_64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    try:
        if cmd == "-save" and len(args) > 2:
            url, filename = args[1], args[2]
            if not url.startswith('http'): url = 'https://' + url
            terminal.insert("end", f"[{NAME}]: Downloading {url}...\n")
            parent.update()
            resp = requests.get(url, headers=headers, timeout=10)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(resp.text)
            terminal.insert("end", f"[{NAME}]: Saved to {filename}\n")

        elif cmd == "-s" and len(args) > 1:
            query = " ".join(args[1:])
            terminal.insert("end", f"[{NAME}]: Searching for '{query}'...\n")
            parent.update()
            url = f"https://html.duckduckgo.com/html/?q={query}"
            resp = requests.get(url, headers=headers, timeout=10)
            
            if resp.status_code != 200:
                terminal.insert("end", f"[{NAME}]: Server error {resp.status_code}\n")
                return

            soup = BeautifulSoup(resp.text, 'html.parser')
            found = False
            for r in soup.find_all('a'):
                href = r.get('href', '')
                title = r.get_text().strip()
                if "uddg=" in href and len(title) > 2:
                    clean_url = unquote(href.split("uddg=")[1].split("&")[0])
                    terminal.insert("end", f"\n> {title}\n  URL: {clean_url}\n")
                    found = True
            
            if not found:
                terminal.insert("end", f"[{NAME}]: No results or parsing failed.\n")

        else:
            url = cmd
            if url.startswith("-"):
                terminal.insert("end", f"[{NAME}]: Unknown flag '{url}'\n")
                return

            if not url.startswith('http'): url = 'https://' + url
            terminal.insert("end", f"[{NAME}]: Opening {url}...\n")
            parent.update()
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            for s in soup(["script", "style"]): s.decompose()
            text = "\n".join([l.strip() for l in soup.get_text().splitlines() if l.strip()])
            terminal.insert("end", f"\n--- {url} ---\n\n")
            terminal.insert("end", text[:5000] + "\n\n--- Content Truncated ---")

    except Exception as e:
        terminal.insert("end", f"[{NAME} ERROR]: {e}\n")
    
    terminal.see("end")
