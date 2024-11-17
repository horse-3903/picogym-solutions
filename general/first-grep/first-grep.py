import sys
sys.path.append("")
from misc.util import save_flag, run_bash

out, err = run_bash(["cat", "general/first-grep/file", "|", "grep", "picoCTF{"])

result = out

dir = save_flag(result, __file__)