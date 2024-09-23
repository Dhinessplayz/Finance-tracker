from database import initialize_db, clear_all_data, get_connection 
from transaction import add_transaction, view_transactions
from budget import set_budget, view_budget
from savings import set_savings_goal, check_savings_goal
from visualization import visualize_spending

def main():
    initialize_db()

    print("Welcome to the Personal Finance Manager!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Set Budget")
        print("4. View Budget")
        print("5. Set Savings Goal")
        print("6. Check Savings Progress")
        print("7. Visualize Spending")
        print("8. CLEAR ALL DATA")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            desc = input("Enter description: ")
            cat = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_transaction(desc, cat, amount)
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            category = input("Enter category: ")
            amount = float(input(f"Set budget for {category}: "))
            set_budget(category, amount)
        elif choice == '4':
            view_budget()
        elif choice == '5':
            goal = float(input("Enter savings goal: "))
            set_savings_goal(goal)
        elif choice == '6':
            goal = float(input("Enter savings goal to check: "))
            check_savings_goal(goal)
        elif choice == '7':
            visualize_spending()
        elif choice == '8':
            confirm = input("Are you sure you want to clear all data (yes/no): ")
            if confirm.lower() == 'yes':
                clear_all_data()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
