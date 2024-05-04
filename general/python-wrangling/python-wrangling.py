import subprocess

pw = None
res = None

with open("./general/python_wrangling/pw.txt", "r") as f:
    pw = f.read()

p = subprocess.Popen(["python", "./general/python_wrangling/ende.py", "-d", "./general/python_wrangling/flag.txt.en"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
comm = p.communicate(pw.encode())

result = comm[0]
result = result.decode()
result = result.strip("\n")

result = result.split(":")[-1]

print(f"Flag found : {result}")