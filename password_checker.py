import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character.")

    # Strength rating
    if strength == 5:
        result = "Strong Password"
    elif strength >= 3:
        result = "Medium Password"
    else:
        result = "Weak Password"

    return result, feedback


print("=== Password Complexity Checker ===")

password = input("Enter your password: ")

result, feedback = check_password_strength(password)

print("\nPassword Strength:", result)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)