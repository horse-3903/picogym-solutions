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

def rot13(s: str) -> str:
    res = ""

    for char in s:
        if not char.isalpha():
            res += char
        elif char.isupper():
            res += chr((ord(char) - 65 + 13) % 26 + 65)
        else:
            res += chr((ord(char) - 97 + 13) % 26 + 97)

    return res

s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"

result = rot13(s)

dir = password_found(result)