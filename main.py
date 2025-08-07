import json

# Initialize the file path
EXPENSE_FILE = 'expenses.json'

# load expenses from the file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            expenses = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        expenses = []
    return expenses

# save expenses to the file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

#------ Add a new expense------
def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter expense items : ")
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.")
    
    expense = {
        'name': name,
        'category': category,
        'amount': amount
    }
    
    # Load existing expenses
    expenses = load_expenses()
    
    # Add the new expense
    expenses.append(expense)
    
    # Save the updated expenses
    save_expenses(expenses)
    
    print(f"Expense '{name}' added successfully!")

#------ View all expenses------
def view_expenses():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n--- Expense List ---")
    for expense in expenses:
        print(f"Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")

#------ Edit an existing expense------
def edit_expense():
    name_to_edit = input("Enter the name of the expense to edit: ")
    
    expenses = load_expenses()
    expense_found = False
    
    for expense in expenses:# Loop through expenses to find the one to edit
        # Check if the expense name matches
        if expense['name'].lower() == name_to_edit.lower():
            expense_found = True
            print(f"Editing expense: {expense['name']}")
            print(f"Current category: {expense['category']}, Current amount: ${expense['amount']:.2f}")
            
            # Ask for new category and amount
            category = input("Enter new category (press Enter to keep current): ")
            if category:
                expense['category'] = category
                
            while True: # Loop until valid amount is entered
                try:
                    amount = input("Enter new amount (press Enter to keep current): ")
                    if amount:
                        expense['amount'] = float(amount)
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number for the amount.")
            
            # Save updated expenses
            save_expenses(expenses)
            print(f"Expense '{expense['name']}' updated successfully!")
            break
    
    if not expense_found:
        print(f"No expense found with the name '{name_to_edit}'.")

#------ Delete an existing expense------

def delete_expense():
    name_to_delete = input("Enter the name of the expense to delete: ")
    
    expenses = load_expenses()
    expenses_after_deletion = [expense for expense in expenses if expense['name'].lower() != name_to_delete.lower()]
    
    if len(expenses) == len(expenses_after_deletion):
        print(f"No expense found with the name '{name_to_delete}'.")
    else:
        save_expenses(expenses_after_deletion)
        print(f"Expense '{name_to_delete}' deleted successfully!")


#------ Show monthly total of expenses------
def show_monthly_total():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    total = sum(expense['amount'] for expense in expenses)
    
    print(f"\n--- Monthly Total ---")
    print(f"Total expenses: ${total:.2f}")

#-------- Show menu options--------
def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Show Monthly Total")
    print("6. Exit")

#-------- Main function to run the program--------
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
