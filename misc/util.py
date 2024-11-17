import subprocess

def save_flag(flag: str, file: str) -> str:
    name = file.split(".")[0]
    
    dir = f"{name}-flag.txt"

    flag = flag.strip()

    print(f"Flag found : {flag}\n")

    print(f"Saving flag to {dir}", end="...")
    
    with open(dir, "w+") as f:
        f.write(flag)

    print("Done\n")

    return dir

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

def git_push(name: str):
    print(f"Running Git Push function", end="...")
    
    command = f'echo "{name}" | commit.bat'
    print(command)
        
    p = subprocess.Popen([command, ], cwd="/".join(__file__.split("\\")[:-1]), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    out, err = p.communicate()

    print("Done\n")
    
    try:
        out, err = out.decode("unicode-escape"), err.decode("unicode-escape")
    except:
        pass
    
    print(out)

    if err:
        print("Error caught : ")
        print(err)
        
if __name__ == "__main__":
    git_push("update : util.py")