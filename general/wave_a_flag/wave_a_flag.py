import subprocess

result = None

file = "./general/wave_a_flag/warm"

p = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = p.communicate(file.encode())

print(f"Output : {stdout}")
print()

p = subprocess.Popen(["bash"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

query = f"{file} -h"
stdout, stderr = p.communicate(query.encode())

print(f"Output : {stdout}")
print()

output = stdout.decode()
output = output.split(": ")

result = output[-1]

print(f"Flag found : {result}")