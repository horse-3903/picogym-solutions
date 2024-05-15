def save_password(pw: str, file: str) -> str:
    name = file.split(".")[0]
    
    dir = f"{name}-flag.txt"

    pw = pw.strip()

    print(f"Password Found : {pw}\n")

    print(f"Saving password to {dir}", end="...")
    
    with open(dir, "w+") as f:
        f.write(pw)

    print("Done\n")

    return dir