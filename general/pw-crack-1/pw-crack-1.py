import sys
sys.path.append("")
from misc.util import save_flag, run_bash

result = None

out, err = run_bash(["echo", "691d", "|", "python3", "general/pw-crack-1/level1.py"])

result = out

dir = save_flag(result, __file__)