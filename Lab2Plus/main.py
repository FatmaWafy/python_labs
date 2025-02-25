import auth  
import projects  

def main():
    print("Welcome to the Crowd-Funding App!")
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            auth.register_user()
        elif choice == "2":
            if auth.login():
                projects.manage_projects()   
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
