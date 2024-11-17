import sys
sys.path.append("")
from util import save_flag, run_bash

result = None

pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]

for pw in pos_pw_list:
    out, err = run_bash(["echo", pw, "|", "python3", "general/pw-crack-3/level3.py"])
    if out and "picoCTF" in out:
        break

result = out

dir = save_flag(result, __file__)