import os
import subprocess

import pwn

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

ssh = pwn.ssh(user="ctf-player", host="venus.picoctf.net", port=50762, password="abcba9f7")

s = ssh.system("ls")

content = s.recv()
content = content.decode()
file3, dir = content.split()

s = ssh.system(f"cat {file3}")
content = s.recv()
pt3 = content.decode()

s = ssh.system(f"cd {dir} && ls")

content = s.recv()
content = content.decode()

file1, file2 = content.split()

s = ssh.system(f"cd {dir} && cat {file1}")
content = s.recv()
pt1 = content.decode()

s = ssh.system(f"cd {dir} && cat {file2}")
content = s.recv()
content = content.decode()

print("\n", content)

s = ssh.system(f"cd / && ls")
content = s.recv()
content = content.decode()

print("\n", content)

s = ssh.system(f"cd / && cat 2of3.flag.txt")
content = s.recv()
pt2 = content.decode()

result = pt1.strip("\n") + pt2.strip("\n") + pt3.strip("\n")

ssh.close()

dir = password_found(result)