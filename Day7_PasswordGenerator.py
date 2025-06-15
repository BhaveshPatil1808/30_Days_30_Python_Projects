import string
import random

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    # Prompt user for password length
    password_length = int(input("Enter the length of the password: \n"))

    # Combine all characters into a single list
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # Shuffle the list to ensure randomness
    random.shuffle(s)

    # Generate and print the password
    print("Your generated password is:")
    print("".join(s[:password_length]))
