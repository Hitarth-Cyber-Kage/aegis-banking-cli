from database import users

def register():
    print("\n--- Register ---")
    
    username = input("Enter username: ").strip()
    
    if username in users:
        print("\nUser already exists. Try logging in.\n")
        return
    
    phone = input("Enter contact number: ").strip()
    email = input("Enter email: ").strip()
    pin = input("Enter 4-digit PIN: ").strip()

    users[username] = {
        "name": username,
        "pin": pin,
        "phone": phone,
        "email": email,
        "balance": 10000
    }

    print("\nRegistration successful!\n")