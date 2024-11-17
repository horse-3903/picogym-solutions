import os
import subprocess

import base64

def run_bash(command: list[str]) -> tuple[str, str] | tuple[bytes, bytes]:
    command = " ".join(command)

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

dir = "./forensics/macrohard-weakedge/"

out, err = run_bash(["binwalk", f'\"{os.path.join(dir, "Forensics is fun.pptm")}\"'])

# out, err = run_bash(["unzip", f'\"{os.path.join(dir, "Forensics is fun.pptm")}\"'])

with open("./forensics/macrohard-weakedge/ppt/vbaProject.bin", "rb") as f:
    content = f.read()

content = content.decode("unicode_escape")
print(content)

with open("./forensics/macrohard-weakedge/ppt/slideMasters/hidden", "r") as f:
    content = f.read()

content = base64.b64decode(content + "==")
content = content.decode()

result = content.split(": ")[-1]

dir = password_found(result)