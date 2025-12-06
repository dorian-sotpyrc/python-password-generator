import secrets
import string

_WORDS = """solar river echo pixel velvet quantum neon forest delta orbit
midnight ember cobalt lunar vector prism turbo crystal apex nova""".split()

def strong_password(length=16, special=True):
    if length < 8:
        raise ValueError("length must be >= 8")
    alphabet = string.ascii_letters + string.digits
    if special:
        alphabet += "!@#$%^&*()-_=+[]{};:,.?/"
    return "".join(secrets.choice(alphabet) for _ in range(length))

def memorable_password(words=4, sep="-", caps=True, number=True):
    if words < 2:
        raise ValueError("words must be >= 2")
    chosen = [secrets.choice(_WORDS) for _ in range(words)]
    if caps:
        chosen = [w.capitalize() for w in chosen]
    pwd = sep.join(chosen)
    if number:
        pwd += sep + str(secrets.randbelow(10**2)).zfill(2)
    return pwd

if __name__ == "__main__":
    print("Choose type: 1=strong, 2=memorable")
    choice = input("Type: ").strip()
    if choice == "1":
        length = input("Length (default 16): ").strip() or "16"
        special = input("Include special chars? [Y/n]: ").strip().lower() or "y"
        pwd = strong_password(int(length), special.startswith("y"))
    elif choice == "2":
        words = input("Words (default 4): ").strip() or "4"
        sep = input("Separator (default '-'): ").strip() or "-"
        number = input("Add trailing number? [Y/n]: ").strip().lower() or "y"
        pwd = memorable_password(int(words), sep=sep, number=number.startswith("y"))
    else:
        raise SystemExit("Invalid choice")
    print("Password:", pwd)
