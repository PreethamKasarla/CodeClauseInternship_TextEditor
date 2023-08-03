import os

def create_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            print(f"File '{filename}' created successfully.")

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(f"--- Content of '{filename}' ---\n{content}")
    else:
        print(f"File '{filename}' not found.")

def update_file(filename):
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            new_content = input("Enter text to append (Press Enter to save and exit): ")
            file.write(new_content)
            print(f"Text appended to '{filename}' successfully.")
    else:
        print(f"File '{filename}' not found.")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    else:
        print(f"File '{filename}' not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Create a new file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            filename = input("Enter the filename to create: ")
            create_file(filename)

        elif choice == '2':
            filename = input("Enter the filename to read: ")
            read_file(filename)

        elif choice == '3':
            filename = input("Enter the filename to update: ")
            update_file(filename)

        elif choice == '4':
            filename = input("Enter the filename to delete: ")
            delete_file(filename)

        elif choice == '5':
            print("Exiting the text editor.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
