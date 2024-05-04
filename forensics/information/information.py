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

img = "./forensics/information/cat.jpg"

out, err = run_bash(["binwalk", "--run-as=root", img])

out, err = run_bash(["strings", img])

out = out.split("<?xpacket end='w'?>")[0]

strings = out.splitlines()
strings = [s.strip() for s in strings if s.strip()]

b64 = ["W5M0MpCehiHzreSzNTczkc9d", "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9"]

for b in b64:
    out, err = run_bash(["echo", f"'{b}'", "|", "base64", "-d"])

    if isinstance(out, bytes):
        continue

    if "pico" in out:
        break

print(f"Password found : {out}")
print()