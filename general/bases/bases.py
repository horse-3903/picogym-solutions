import sys

sys.path.append("")

from util import save_flag
import base64

b64_str = "bDNhcm5fdGgzX3IwcDM1"

decoded_bytes = base64.b64decode(b64_str)
result = f"picoCTF{'{' + str(decoded_bytes)[2:-1] + '}'}"

dir = save_flag(result, __file__)