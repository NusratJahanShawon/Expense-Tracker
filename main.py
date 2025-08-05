def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Show Monthly Total")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            edit_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            show_monthly_total()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
