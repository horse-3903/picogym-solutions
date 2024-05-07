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

dir = "./forensics/matrykosha-doll"

# 1st layer
out, err = run_bash(["binwalk", "--run-as=root", dir + "/dolls.jpg"])

# out, err = run_bash(["binwalk", "--run-as=root", "-e", img])

if not os.path.exists(dir + "/_dolls.jpg.extracted"):
    out, err = run_bash(["binwalk", "--run-as=root", "-e", dir + "/dolls.jpg"])

out, err = run_bash(["echo", "y", "|", "unzip", dir + "/_dolls.jpg.extracted/4286C.zip"])

# 2nd layer
out, err = run_bash(["binwalk", "--run-as=root", dir + "/_dolls.jpg.extracted/base_images/2_c.jpg"])

if not os.path.exists(dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted"):
    out, err = run_bash(["binwalk", "--run-as=root", "-e", dir + "/_dolls.jpg.extracted/base_images/2_c.jpg"])

out, err = run_bash(["unzip", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/2DD3B.zip"])

# 3rd layer
out, err = run_bash(["binwalk", "--run-as=root", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/3_c.jpg"])

if not os.path.exists(dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted"):
    out, err = run_bash(["binwalk", "--run-as=root", "-e", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/3_c.jpg"])

out, err = run_bash(["unzip", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/1E2D6.zip"])

# 4th layer
out, err = run_bash(["binwalk", "--run-as=root", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/4_c.jpg"])

if not os.path.exists(dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted"):
    out, err = run_bash(["binwalk", "--run-as=root", "-e", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/4_c.jpg"])

out, err = run_bash(["unzip", dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/136DA.zip"])

with open(dir + "/_dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt", "rb") as f:
    data = f.read()

result = data.decode()

dir = password_found(result)