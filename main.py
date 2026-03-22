from login import login
from register import register

def main():
    while True:
        print("=== AEGIS Banking CLI ===")
        print("1) Login")
        print("2) Register")
        print("3) Exit")

        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            user = login()
            if user:
                dashboard(user)

        elif choice == "2":
            register()

        elif choice == "3":
            print("\nExiting AEGIS...\n")
            break

        else:
            print("\nInvalid option.\n")


def dashboard(username):
    print(f"\nWelcome, {username}!")
    print("Dashboard coming soon...\n")


if __name__ == "__main__":
    main()
