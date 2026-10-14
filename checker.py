from getpass import getpass

with open("common_passwords.txt", encoding="utf-8", errors="ignore") as file:
    common_passwords = set(line.strip().lower() for line in file)

password = getpass("what is your password?\n ")
length = len(password)
print(f"-Your password is {length} characters long")

if length < 8:
    print("Your password is too short\n")
elif length < 12:
    print("Your password is okay but 12+ is better\n")
else:
    print("Your password is Good\n")

#to check if the password has symbols,uppercase,lowercase or digits

has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digits = any(c.isdigit() for c in password)
has_symbols = any( not c.isalnum() for c in password)

print("lowercase:", has_lower)
print("uppercase:", has_upper)
print("digits:", has_digits)
print("symbols:", has_symbols)

#give the password a score

score = 0
feedback = []

# Length
if length >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

if length >= 12:
    score += 1
else:
    feedback.append("12 or more characters is much stronger.")

# Character types
if has_lower:
    score += 1
else:
    feedback.append("Add lowercase letters.")

if has_upper:
    score += 1
else:
    feedback.append("Add uppercase letters.")

if has_digits:
    score += 1
else:
    feedback.append("Add some numbers.")

if has_symbols:
    score += 1
else:
    feedback.append("Add symbols like ! @ # $.")

if password.lower() in common_passwords:
    score = 0
    feedback.insert(0, "This is one of the most common passwords. Attackers try these first, so it can be cracked almost instantly.")

print(f"Score: {score}/6")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")

if feedback:
    print("\nHow to improve it:")
    for tip in feedback:
        print(f"- {tip}")
else:
    print("\nNo suggestions. Nice password!")