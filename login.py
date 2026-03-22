from database import users

def login():
    print("\n--- Login ---")
    
    username = input("Enter username: ").strip()
    pin = input("Enter 4-digit PIN: ").strip()

    if username in users:
        if users[username]["pin"] == pin:
            print("\nLogin successful!\n")
            return username
        else:
            print("\nWrong PIN.\n")
            return None
    else:
        print("\nUser not found.\n")
        return None