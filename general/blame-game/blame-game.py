import os
import sys

sys.path.append(".")

from misc.util import *

cur_dir = os.path.dirname(__file__).replace("\\", "/")
cur_dir = "." + cur_dir.split("picogym-solutions")[-1]

out, err = run_bash(["cd", cur_dir + "/drop-in", "&&", "git", "log"])

out, err = run_bash(["cd", cur_dir + "/drop-in", "&&", "git", "log", "|", "grep", "picoCTF{"])

result = out[out.find("picoCTF{"):out.find("}")+1]

dir = save_password(result, __file__)