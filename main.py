import re

# Predefined list of common fake domains
blacklisted_domains = ["test.com", "example.com", "invalid.com"]

email = input("Enter your email: ")

# Step 1: Basic Length Check
if len(email) < 6:
    print("Error: Email length should be at least 6 characters")
else:
    # Step 2: Regex Pattern Check for Advanced Validation
    pattern = r"^[a-zA-Z][a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,3}$"
    if not re.match(pattern, email):
        print("Error: Email pattern is invalid. Must start with alphabet and contain '@' and '.' in correct positions.")
    else:
        # Step 3: Special Character Validation
        if " " in email:
            print("Error: Spaces are not allowed in email.")
        elif any(char.isupper() for char in email):
            print("Error: Uppercase letters are not allowed in email.")
        else:
            # Step 4: Domain Specific Checks
            domain = email.split('@')[-1]
            if domain in blacklisted_domains:
                print(f"Error: '{domain}' is a blacklisted domain.")
            elif ".." in email or email[email.find('@')+1] == '.':
                print("Error: Invalid placement of '.' character.")
            else:
                print("Email is valid and passed all advanced checks.")
