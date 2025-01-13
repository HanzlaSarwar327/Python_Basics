# Email Slicer

def slice_email(email):
    try:
        username, domain = email.split("@")
        return username, domain
    except ValueError:
        print("Error: Invalid email address format.")
        return None, None

def email_slicer():
    print("Welcome to the Email Slicer!")
    email = input("Enter your email address: ")
    username, domain = slice_email(email)
    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")

if __name__ == "__main__":
    email_slicer()
