import os
import sys

sys.path.append(".")

from misc.util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("picogym-solutions")[-1]

out, err = run_bash(["cd", cur_dir + "/drop-in", "&&", "git", "branch"])
branches = out.splitlines()[:-1]
branches = [b.strip() for b in branches]

for b in branches:
    out, err = run_bash(["cd", cur_dir + "/drop-in", "&&", "git", "checkout", b])
    out, err = run_bash(["cd", cur_dir + "/drop-in", "&&", "git", "checkout", b])

# dir = save_password(result, __file__)