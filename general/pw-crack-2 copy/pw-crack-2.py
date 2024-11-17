import sys
sys.path.append("")
from misc.util import save_flag, run_bash

result = None

pw = chr(0x33) + chr(0x39) + chr(0x63) + chr(0x65)

out, err = run_bash(["echo", pw, "|", "python3", "general/pw-crack-2/level2.py"])

result = out

dir = save_flag(result, __file__)