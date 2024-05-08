import os
import subprocess

def run_bash(command: list[str]) -> tuple[str, str] | tuple[bytes, bytes]:
    command = " ".join(command)

    print(f"Running bash command : `{command}`", end="...")
    
    p = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = p.communicate(command.encode())

    print("Done\n")
    
    try:
        out, err = out.decode("unicode-escape"), err.decode("unicode-escape")
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

out, err = run_bash(["cd", "./general/commitment-issues/drop-in", "&&", "git", "log"])

log = out.split("commit ")
log = log[1:]
log = [[t.strip() for t in c.split("\n") if t] for c in log]

commit = log[1]

out, err = run_bash(["cd", "./general/commitment-issues/drop-in", "&&", "git", "show", commit[0]])

info = out.splitlines()
info = info[-1]
result = info.strip("+")

dir = password_found(result)