def display_menu():
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                item_name = input("Enter the item to add: ")
                shopping_list.append(item_name)
                print("Current list:", shopping_list)

                add_more = input("Do you want to add another item? (yes/no): ")
                if add_more != 'yes':
                    break

        elif choice == '2':
            item_name = input("Remove your item: ")
            if item_name in shopping_list:
                shopping_list.remove(item_name)
                print("Item removed. Updated list:", shopping_list)
            else:
                print(f"{item_name} is not in your list.")

        elif choice == '3':
            print("Your Shopping List:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

        elif choice == '4':
            print("Goodbye!")
            print(f"Your final shopping list: {shopping_list}")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
