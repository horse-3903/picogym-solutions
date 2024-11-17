import os
import subprocess

from bs4 import BeautifulSoup

def run_bash(command: list[str]) -> tuple[str, str] | tuple[bytes, bytes]:
    command = " ".join(map(str, command))

    print(f"Running bash command : `{command}`", end="...")
    
    p = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = p.communicate(command.encode(), timeout=None)

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

dir = "./forensics/enhance/"

with open(os.path.join(dir, "drawing.flag.svg"), "r") as f:
    content = f.read()

soup = BeautifulSoup(content, features="xml")

text = soup.get_text(separator="")
text = [*filter(lambda s: s, text.splitlines())]
text = text[-1].split()

result = "".join(text)

dir = password_found(result)