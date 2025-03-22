import os

while True:
    print("\n1. Create  2. Read  3. Append  4. Delete  5. Exit")
    choice = input("Choose (1-5): ")

    if choice == '1':
        with open(input("File name: "), 'w') as f: f.write(input("Content: "))
    elif choice == '2':
        file = input("File name: ")
        print(open(file).read() if os.path.exists(file) else "File not found.")
    elif choice == '3':
        file = input("File name: ")
        if os.path.exists(file):
            with open(file, 'a') as f: f.write(input("Content to append: "))
        else: print("File not found.")
    elif choice == '4':
        file = input("File name: ")
        os.remove(file) if os.path.exists(file) else print("File not found.")
    elif choice == '5':
        print("Goodbye!"); break
    else:
        print("Invalid choice.")
