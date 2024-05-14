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

dir = "./forensics/disk-disk-sleuth-2/"
file = "dds2-alpine.flag.img"

out, err = run_bash(["cd", dir, "&&", "gunzip", file + ".gz"])

out, err = run_bash(["cd", dir, "&&", "mmls", file])

out = out.splitlines()[5:]
out = [o.split()[2] for o in out]

for offset in out:
    out, err = run_bash(["fls", "-o", int(offset), os.path.join(dir, file)])

    if "root" in out:
        break

out = out.replace(":", "")
out = out.splitlines()
out = [o.split() for o in out]

print(out)

for func, inum, path in out:
    if "root" in path:
        out, err = run_bash(["fls", "-o", int(offset), os.path.join(dir, file), inum])
        break

out = out.replace(":", "")
out = out.splitlines()
out = [o.split() for o in out]

for func, inum, path in out:
    if "down-at-the-bottom.txt" in path:
        out, err = run_bash(["icat", "-o", int(offset), os.path.join(dir, file), inum])
        break

out = out.splitlines()
out = "".join(out[2::4])

for c in ["(", " ", ")"]:
    out = out.replace(c, "")

result = out

dir = password_found(result)