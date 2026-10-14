import string
import secrets


def analyze_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters (A-Z).")

    # Check lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters (a-z).")

    # Check numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers (0-9).")

    # Check special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters (!, @, #).")

    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    print("\n--- Password Analysis ---")
    print("Length:", len(password))
    print("Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Your password meets all basic checks!")


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(
            secrets.choice(characters) for _ in range(length)
        )

        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            return password


print("===== PASSWORD STRENGTH ANALYZER =====")
print("1. Check password strength")
print("2. Generate a random password")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    password = input("Enter a test password: ")
    analyze_password(password)

elif choice == "2":
    print("\nGenerated password:", generate_password())
    print("Store it securely and do not share it.")

else:
    print("Invalid choice. Please select 1 or 2.")