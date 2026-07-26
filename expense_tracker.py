# Personal Expense Tracker
# CloudExify Python Internship 2026 - Month 1 Project 1
# Name: [SYEDA RIDA FATIMA]
# Reg No: CX-INT-2026-PY-0362

# This list will hold all my expenses while the program is running
expense_list = []
current_id = 1

categories = ["Food", "Transport", "Shopping", "Bills", "Other"]


def add_expense():
    global current_id

    print("\n--- Add New Expense ---")
    desc = input("Enter description: ")

    # keep asking until user enters a proper positive number
    while True:
        amount_text = input("Enter amount (PKR): ")
        try:
            amount = float(amount_text)
        except ValueError:
            print("Please enter numbers only!")
            continue

        if amount <= 0:
            print("Amount must be more than 0!")
            continue

        break

    print("Choose a category:")
    for i in range(len(categories)):
        print(str(i + 1) + ". " + categories[i])

    while True:
        cat_choice = input("Enter category number: ")
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        else:
            print("Please choose a valid number from the list.")

    new_expense = {
        "id": current_id,
        "desc": desc,
        "amount": amount,
        "category": category
    }

    expense_list.append(new_expense)
    print("Expense added successfully! ID:", current_id)
    current_id = current_id + 1


def view_expenses():
    print("\n--- All Expenses ---")

    if len(expense_list) == 0:
        print("No expenses added yet.")
        return

    print("ID   Description         Category     Amount")
    print("---------------------------------------------")

    total = 0
    for e in expense_list:
        print(str(e["id"]) + "    " + e["desc"] + "    " + e["category"] + "    " + str(e["amount"]))
        total = total + e["amount"]

    print("---------------------------------------------")
    print("Total spent: PKR", total)


def category_summary():
    print("\n--- Category Summary ---")

    if len(expense_list) == 0:
        print("No expenses to show yet.")
        return

    summary = {}
    for e in expense_list:
        cat = e["category"]
        if cat in summary:
            summary[cat] = summary[cat] + e["amount"]
        else:
            summary[cat] = e["amount"]

    total = 0
    for e in expense_list:
        total = total + e["amount"]

    for cat in summary:
        percent = (summary[cat] / total) * 100
        print(cat, ": PKR", summary[cat], "(", round(percent, 1), "%)")


def filter_by_category():
    print("\n--- Filter By Category ---")

    if len(expense_list) == 0:
        print("No expenses added yet.")
        return

    search_cat = input("Enter category to search: ")

    found = False
    total = 0
    print("ID   Description         Amount")
    print("--------------------------------")

    for e in expense_list:
        if e["category"].lower() == search_cat.lower():
            print(str(e["id"]) + "    " + e["desc"] + "    " + str(e["amount"]))
            total = total + e["amount"]
            found = True

    if found == False:
        print("No expenses found in this category.")
    else:
        print("--------------------------------")
        print("Total for", search_cat, ": PKR", total)


def delete_expense():
    print("\n--- Delete Expense ---")

    if len(expense_list) == 0:
        print("No expenses to delete.")
        return

    view_expenses()
    del_id = input("\nEnter ID of expense to delete: ")

    if not del_id.isdigit():
        print("Please enter a valid ID number.")
        return

    del_id = int(del_id)
    found = False

    for e in expense_list:
        if e["id"] == del_id:
            confirm = input("Are you sure you want to delete '" + e["desc"] + "'? (y/n): ")
            if confirm.lower() == "y":
                expense_list.remove(e)
                print("Expense deleted.")
            else:
                print("Delete cancelled.")
            found = True
            break

    if found == False:
        print("No expense found with that ID.")


def save_expenses():
    file = open("expenses.txt", "w")
    for e in expense_list:
        line = str(e["id"]) + "," + e["desc"] + "," + str(e["amount"]) + "," + e["category"] + "\n"
        file.write(line)
    file.close()
    print("Expenses saved to file.")


def load_expenses():
    global current_id

    try:
        file = open("expenses.txt", "r")
    except FileNotFoundError:
        return

    for line in file:
        line = line.strip()
        if line == "":
            continue

        parts = line.split(",")
        expense = {
            "id": int(parts[0]),
            "desc": parts[1],
            "amount": float(parts[2]),
            "category": parts[3]
        }
        expense_list.append(expense)
        current_id = int(parts[0]) + 1

    file.close()


def show_menu():
    print("\n===========================")
    print("   EXPENSE TRACKER MENU")
    print("===========================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Save Expenses")
    print("7. Exit")
    print("===========================")


def main():
    print("Loading saved expenses...")
    load_expenses()
    print("Loaded", len(expense_list), "expenses.\n")

    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_summary()
        elif choice == "4":
            filter_by_category()
        elif choice == "5":
            delete_expense()
        elif choice == "6":
            save_expenses()
        elif choice == "7":
            save_expenses()
            print("Goodbye! Your expenses have been saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


main()
