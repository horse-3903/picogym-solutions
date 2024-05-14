import os
import subprocess

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

dir = "./forensics/disk-disk-sleuth/"

out, err = run_bash(["cd", dir, "&&", "gunzip", "dds1-alpine.flag.img.gz"])

out, err = run_bash(["cat", os.path.join(dir, "dds1-alpine.flag.img"), "|", "grep", "--text", "picoCTF{"])

out = out.split()[-1]
result = out.strip()

dir = password_found(result)