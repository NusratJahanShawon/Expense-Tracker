#---------------Adding Expenses---------
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
