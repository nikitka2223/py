import os
import zipfile

def run(parent, args, terminal):
    if not args:
        terminal.insert("end", "Usage: unzip <file.zip> [-p path] [-d folder_name]\n")
        return

    zip_src = args[0]
    if not os.path.exists(zip_src):
        terminal.insert("end", f"Error: File {zip_src} not found.\n")
        return

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dest_path = os.path.join(base_dir, "vfs")
    folder_name = os.path.splitext(os.path.basename(zip_src))[0]

    if "-p" in args:
        try:
            rel_path = args[args.index("-p") + 1]
            dest_path = os.path.join(base_dir, rel_path)
        except IndexError: pass
            
    if "-d" in args:
        try:
            folder_name = args[args.index("-d") + 1]
        except IndexError: pass

    final_dest = os.path.join(dest_path, folder_name)

    try:
        terminal.insert("end", f"Extracting to: {final_dest}...\n")
        parent.update()
        
        with zipfile.ZipFile(zip_src, 'r') as zip_ref:
            zip_ref.extractall(final_dest)
            
        terminal.insert("end", f"Unzip Success: {len(zip_ref.namelist())} files extracted.\n")
    except Exception as e:
        terminal.insert("end", f"Unzip Error: {e}\n")