import os
import subprocess

def run_bash(command: list[str]) -> tuple[str, str]:
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

pw = None
res = None

with open("./general/python-wrangling/pw.txt", "r") as f:
    pw = f.read()

p = subprocess.Popen(["python", "./general/python-wrangling/ende.py", "-d", "./general/python-wrangling/flag.txt.en"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
comm = p.communicate(pw.encode())

result = comm[0]
result = result.decode()
result = result.strip("\n")

result = result.split(":")[-1]

dir = password_found(result)