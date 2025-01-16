import re

def password_strength(password):
    # Initialize strength score
    strength = 0

    # Check password length
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1

    # Check for digits
    if re.search(r'\d', password):
        strength += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    # Provide feedback based on strength score
    if strength <= 2:
        return "Weak password. Consider making it longer and including more complexity."
    elif strength == 3:
        return "Moderate password. It could be improved by adding more variety."
    elif strength == 4:
        return "Strong password. You're doing great!"
    else:
        return "Very strong password. Excellent!"

# Test the password strength checker
password = input("Enter your password to check its strength: ")
print(password_strength(password))
