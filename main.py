import json
from datetime import datetime, date

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
    
    # Get date input
    while True:
        date_input = input("Enter expense date (YYYY-MM-DD) or press Enter for today: ")
        if not date_input:
            expense_date = date.today().isoformat()
            break
        try:
            # Validate date format
            datetime.strptime(date_input, '%Y-%m-%d')
            expense_date = date_input
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD format.")
    
    while True:
        try:
            amount = float(input("Enter expense amount: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.")
    
    # Show confirmation
    print(f"\n--- Expense Summary ---")
    print(f"Name: {name}")
    print(f"Category: {category}")
    print(f"Amount: ${amount:.2f}")
    print(f"Date: {expense_date}")
    
    # Ask for confirmation
    while True:
        confirm = input("\nDo you want to save this expense? (y/n): ").lower().strip()
        if confirm in ['y', 'yes']:
            expense = {
                'name': name,
                'category': category,
                'amount': amount,
                'date': expense_date
            }
            
            # Load existing expenses
            expenses = load_expenses()
            
            # Add the new expense
            expenses.append(expense)
            
            # Save the updated expenses
            save_expenses(expenses)
            
            print(f"Expense '{name}' added successfully on {expense_date}!")
            break
        elif confirm in ['n', 'no']:
            print("Expense cancelled. No changes made.")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

#------ View all expenses------
def view_expenses():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n--- Expense List ---")
    for i, expense in enumerate(expenses, 1):
        date_str = expense.get('date', 'No date')
        print(f"{i}. Date: {date_str}, Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")

#------ Edit an existing expense------
def edit_expense():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found to edit.")
        return
    
    # Show numbered list of expenses
    print("\n--- Select Expense to Edit ---")
    print("0. Go Back")
    for i, expense in enumerate(expenses, 1):
        date_str = expense.get('date', 'No date')
        print(f"{i}. Date: {date_str}, Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
    
    # Get user selection
    while True:
        try:
            choice = int(input(f"\nEnter the number of the expense to edit (0-{len(expenses)}): "))
            if choice == 0:
                print("Going back to main menu...")
                return
            elif 1 <= choice <= len(expenses):
                break
            else:
                print(f"Please enter a number between 0 and {len(expenses)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get the selected expense
    selected_expense = expenses[choice - 1]
    current_date = selected_expense.get('date', 'No date')
    current_category = selected_expense['category']
    current_amount = selected_expense['amount']
    
    print(f"\nEditing expense: {selected_expense['name']}")
    print(f"Current date: {current_date}, Current category: {current_category}, Current amount: ${current_amount:.2f}")
    
    # Ask for new date, category and amount
    date_input = input("Enter new date (YYYY-MM-DD, press Enter to keep current): ")
    if date_input:
        try:
            datetime.strptime(date_input, '%Y-%m-%d')
            selected_expense['date'] = date_input
        except ValueError:
            print("Invalid date format! Date not updated.")
    
    category = input("Enter new category (press Enter to keep current): ")
    if category:
        selected_expense['category'] = category
        
    while True: # Loop until valid amount is entered
        try:
            amount = input("Enter new amount (press Enter to keep current): ")
            if amount:
                selected_expense['amount'] = float(amount)
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the amount.")
    
    # Show updated expense summary
    updated_date = selected_expense.get('date', 'No date')
    updated_category = selected_expense.get('category', 'No category')
    updated_amount = selected_expense.get('amount', 0)
    
    print(f"\n--- Updated Expense Summary ---")
    print(f"Name: {selected_expense['name']}")
    print(f"Category: {updated_category}")
    print(f"Amount: ${updated_amount:.2f}")
    print(f"Date: {updated_date}")
    
    # Ask for confirmation
    while True:
        confirm = input("\nDo you want to save these changes? (y/n): ").lower().strip()
        if confirm in ['y', 'yes']:
            # Save updated expenses
            save_expenses(expenses)
            print(f"Expense '{selected_expense['name']}' updated successfully!")
            break
        elif confirm in ['n', 'no']:
            print("Changes cancelled. No updates made.")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

#------ Delete an existing expense------
def delete_expense():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found to delete.")
        return
    
    # Show numbered list of expenses
    print("\n--- Select Expense to Delete ---")
    print("0. Go Back")
    for i, expense in enumerate(expenses, 1):
        date_str = expense.get('date', 'No date')
        print(f"{i}. Date: {date_str}, Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
    
    # Get user selection
    while True:
        try:
            choice = int(input(f"\nEnter the number of the expense to delete (0-{len(expenses)}): "))
            if choice == 0:
                print("Going back to main menu...")
                return
            elif 1 <= choice <= len(expenses):
                break
            else:
                print(f"Please enter a number between 0 and {len(expenses)}.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get the selected expense
    selected_expense = expenses[choice - 1]
    
    # Show expense details for confirmation
    print(f"\n--- Expense to Delete ---")
    print(f"Name: {selected_expense['name']}")
    print(f"Category: {selected_expense['category']}")
    print(f"Amount: ${selected_expense['amount']:.2f}")
    print(f"Date: {selected_expense.get('date', 'No date')}")
    
    # Ask for confirmation
    while True:
        confirm = input(f"\nAre you sure you want to delete '{selected_expense['name']}'? (y/n): ").lower().strip()
        if confirm in ['y', 'yes']:
            expenses_after_deletion = [expense for expense in expenses if expense != selected_expense]
            save_expenses(expenses_after_deletion)
            print(f"Expense '{selected_expense['name']}' deleted successfully!")
            break
        elif confirm in ['n', 'no']:
            print("Deletion cancelled. No changes made.")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

#------ Show monthly total of expenses------
def show_monthly_total():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    # Ask user which month to view
    print("\n--- Monthly Total ---")
    print("1. Current month")
    print("2. Specific month")
    
    while True:
        choice = input("Enter your choice (1-2): ").strip()
        if choice == '1':
            # Get current month and year
            target_month = date.today().month
            target_year = date.today().year
            break
        elif choice == '2':
            # Get specific month and year
            while True:
                month_input = input("Enter month (1-12): ")
                try:
                    target_month = int(month_input)
                    if 1 <= target_month <= 12:
                        break
                    else:
                        print("Month must be between 1 and 12.")
                except ValueError:
                    print("Please enter a valid number for month.")
            
            while True:
                year_input = input("Enter year (YYYY): ")
                try:
                    target_year = int(year_input)
                    if 1900 <= target_year <= 2100:
                        break
                    else:
                        print("Year must be between 1900 and 2100.")
                except ValueError:
                    print("Please enter a valid number for year.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    
    monthly_expenses = []
    total = 0
    
    for expense in expenses:
        expense_date = expense.get('date')
        if expense_date:
            try:
                expense_datetime = datetime.strptime(expense_date, '%Y-%m-%d').date()
                if expense_datetime.month == target_month and expense_datetime.year == target_year:
                    monthly_expenses.append(expense)
                    total += expense['amount']
            except ValueError:
                continue
    
    # Get month name
    month_names = ["", "January", "February", "March", "April", "May", "June",
                   "July", "August", "September", "October", "November", "December"]
    
    print(f"\n--- Monthly Total for {month_names[target_month]} {target_year} ---")
    if monthly_expenses:
        print(f"Number of expenses: {len(monthly_expenses)}")
        print(f"Total expenses: ${total:.2f}")
        
        # Show breakdown by category
        category_totals = {}
        for expense in monthly_expenses:
            category = expense['category']
            category_totals[category] = category_totals.get(category, 0) + expense['amount']
        
        print("\nBreakdown by category:")
        for category, amount in category_totals.items():
            print(f"  {category}: ${amount:.2f}")
        
        # Show all expenses for the month
        print(f"\nAll expenses for {month_names[target_month]} {target_year}:")
        for expense in monthly_expenses:
            date_str = expense.get('date', 'No date')
            print(f"  {date_str}: {expense['name']} - {expense['category']} - ${expense['amount']:.2f}")
    else:
        print(f"No expenses found for {month_names[target_month]} {target_year}.")

#------ Filter expenses by date range------
def filter_expenses_by_date():
    print("\n--- Filter Expenses by Date Range ---")
    
    while True:
        start_date_input = input("Enter start date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date_input, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD format.")
    
    while True:
        end_date_input = input("Enter end date (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date_input, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD format.")
    
    if start_date > end_date:
        print("Start date cannot be after end date!")
        return
    
    expenses = load_expenses()
    filtered_expenses = []
    total = 0
    
    for expense in expenses:
        expense_date = expense.get('date')
        if expense_date:
            try:
                expense_datetime = datetime.strptime(expense_date, '%Y-%m-%d').date()
                if start_date <= expense_datetime <= end_date:
                    filtered_expenses.append(expense)
                    total += expense['amount']
            except ValueError:
                continue
    
    print(f"\n--- Expenses from {start_date} to {end_date} ---")
    if filtered_expenses:
        print(f"Number of expenses: {len(filtered_expenses)}")
        print(f"Total amount: ${total:.2f}")
        print("\nExpense details:")
        for expense in filtered_expenses:
            date_str = expense.get('date', 'No date')
            print(f"  Date: {date_str}, Name: {expense['name']}, Category: {expense['category']}, Amount: ${expense['amount']:.2f}")
    else:
        print("No expenses found in the specified date range.")

#-------- Show menu options--------
def show_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Show Monthly Total")
    print("6. Filter Expenses by Date")
    print("7. Exit")

#-------- Main function to run the program--------
def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

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
            filter_expenses_by_date()
        elif choice == '7':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
