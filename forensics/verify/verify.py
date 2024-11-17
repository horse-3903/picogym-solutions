import os
import subprocess

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

dir = "./forensics/verify/dropin/"

out, err = run_bash(["sha256sum", os.path.join(dir, "files/*")])

with open(os.path.join(dir, "checksum.txt"), "r") as f:
    checksum = f.read()

out, err = run_bash(["sha256sum", os.path.join(dir, "files/*"), "|", "grep", checksum])
checksum, file = out.split()

file = file.split("/")[-1]

out, err = run_bash(["cd", dir, "&&", "./decrypt.sh", file])

result = out

dir = password_found(result)