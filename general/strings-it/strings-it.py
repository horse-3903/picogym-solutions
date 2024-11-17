import sys
sys.path.append("")
from misc.util import save_flag, run_bash

out, err = run_bash(["strings", "general/strings-it/strings", "|", "grep", "picoCTF{"])

result = out

dir = save_flag(result, __file__)