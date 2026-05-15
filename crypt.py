def run(parent, args, terminal):
    if len(args) < 2:
        terminal.insert("end", "Usage: crypt <filename> <key>\n")
        return
    
    path, key = args[0], args[1]
    try:
        with open(path, 'rb') as f:
            data = f.read()
        
        encrypted = bytearray(b ^ ord(key[i % len(key)]) for i, b in enumerate(data))
        
        with open(path, 'wb') as f:
            f.write(encrypted)
            
        terminal.insert("end", f"Done! File '{path}' processed.\n")
    except Exception as e:
        terminal.insert("end", f"Error: {e}\n")
