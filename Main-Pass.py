import random
from datetime import datetime

# Character sets
Lowercase = 'abcdefghijklmnopqrstuvwxyz'
Uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Digit = '0123456789'
Punctuation = '!@#$%^&*()-_=+[]{};:,.<>?/'

def generate_password(length=16):
    if length < 4:
        raise ValueError("Password must be at least 4 characters to include all types.")

    # Ensure at least one character from each type
    password = [
        random.choice(Lowercase),
        random.choice(Uppercase),
        random.choice(Digit),
        random.choice(Punctuation)
    ]

    # Fill remaining characters
    all_chars = Lowercase + Uppercase + Digit + Punctuation
    password += [random.choice(all_chars) for _ in range(length - 4)]

    # Shuffle the list and convert to string
    random.shuffle(password)
    return ''.join(password)

def save_password(password):
    date_str = datetime.now().strftime("%Y-%m-%d")
    with open("weekly_passwords.txt", "a") as file:
        file.write(f"{date_str} - {password}\n")

def main():
    # Run only on Friday
    
    if datetime.now().weekday() == 4:  # 4 = Friday
        password = generate_password()
        save_password(password)
        print("Weekly password generated:", password)
    else:
        print("Today is not Friday. No password generated.")

if __name__ == "__main__":
    main()