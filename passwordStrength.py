import re

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password at least 8 characters ka hona chahiye")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("At least 1 uppercase letter add karo")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("At least 1 lowercase letter add karo")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("At least 1 number add karo")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("At least 1 special character add karo")

    print("\n🔐 Password Strength Result:")

    if score == 5:
        print("✅ Strong Password 💪")
    elif score >= 3:
        print("⚠️ Medium Password")
    else:
        print("❌ Weak Password")

    print(f"Score: {score}/5")

    if suggestions:
        print("\n💡 Suggestions:")
        for s in suggestions:
            print("→", s)


if __name__ == "__main__":
    password = input("Enter your password: ")
    check_password_strength(password)