import os
import subprocess

import pcapng
import pcapng.blocks

def run_bash(command: list[str]) -> tuple[str, str] | tuple[bytes, bytes]:
    command = " ".join(command)

    print(f"Running bash command : `{command}`", end="...")
    
    p = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = p.communicate(command.encode())

    print("Done\n")
    
    try:
        out, err = out.decode(), err.decode()
    except:
        pass

    if not err:
        print("Output received : ")
        print(out or None)
    else:
        print("Error caught : ")
        print(err)

    print()

    return out, err

def password_found(pw: str) -> str:
    name = __file__.split(".")[0]
    
    dir = f"{name}-flag.txt"

    print(f"Password Found : {pw}\n")

    print(f"Saving password to {dir}", end="...")
    
    with open(dir, "w+") as f:
        f.write(pw)

    print("Done\n")

    return dir

with open("./forensics/wireshark-doo-doo/shark1.pcapng", "rb") as f:
    scan = pcapng.FileScanner(f)
    scan = [*scan]

packet = [p.packet_data for p in scan if type(p) == pcapng.blocks.EnhancedPacket]
packet = [p for p in packet if b"Content-Type: text/html" in p][0]
packet = packet.decode("unicode-escape")
packet = "".join([p for p in packet if p.isprintable()])
data = packet.split()[-1]
    
rot13 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
result = str.translate(data, rot13)
dir = password_found(result)