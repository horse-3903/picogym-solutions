s = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"

def rot13(s: str) -> str:
    res = ""

    for char in s:
        if not char.isalpha():
            res += char
        elif char.isupper():
            res += chr((ord(char) - 65 + 13) % 26 + 65)
        else:
            res += chr((ord(char) - 97 + 13) % 26 + 97)

    return res

print(rot13(s))