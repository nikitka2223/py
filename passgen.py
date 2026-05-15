import random, string, sys

def run(parent, args, terminal):
    length = int(args[0]) if args else 12
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    terminal.insert("end", f"Generated password: {password}\n")
