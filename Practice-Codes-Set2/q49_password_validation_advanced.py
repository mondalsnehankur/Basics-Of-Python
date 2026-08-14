# Q49. Password Validation System (Advanced)

password = "Secure@9"
has_length = len(password) >= 8
has_at = "@" in password
has_digit = any(c.isdigit() for c in password)

if has_length and has_at and has_digit:
    print("Password Status : Valid")
else:
    print("Password Status : Invalid")
    if not has_length:
        print("  - Minimum 8 characters required")
    if not has_at:
        print("  - '@' symbol required")
    if not has_digit:
        print("  - At least one digit required")
