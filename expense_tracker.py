import csv

print("====== EXPENSES TRACKER =====\n")

expenses = {}
FILE_NAME = "expense.csv"

def load_expenses():
    try:
        with open(FILE_NAME , "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    continue   

                category = row[0]

                try:
                    amount = int(row[1])
                except ValueError:
                    continue   
                    
                expenses[category] = amount

    except FileNotFoundError:
        pass
        
def save_expenses():
    with open(FILE_NAME , "w", newline="") as file:
        writer = csv.writer(file)
        for category, amount in expenses.items():
            writer.writerow([category, amount])

load_expenses()

def user_choice():
	user_choice = input("Enter the index of work you wanna do:\n")
	return user_choice
	
def add_expense():		
	add_category = input("Enter the category of expense\n").lower()
	
	if add_category == "":
		print("Category can't be empty\n")
		return
		
	try:
		amount_category = int(input("Enter the amount of expense\n"))
	except ValueError:			
		print("Amount must be in integers\n")
		return
						
	if add_category in expenses:
		expenses[add_category] += amount_category
		print("Expense list updated\n")
	else:
		expenses[add_category] = amount_category
		print("New expense added\n")
	save_expenses()
		
def view_expense():
	expenses_sum = 0
		
	if not expenses:
		print("No expenses yet\n")
		return
		
	print("Your expenses: \n")
	for c, a in expenses.items():
		print(f"{c.capitalize()} : ${a}\n")
		expenses_sum += a

	avg_expenses = expenses_sum/len(expenses)
			
	print(f"Total number of categories : {len(expenses)}\n")
	print(f"Total amount spent : {expenses_sum}\n")
	print(f"Average amount spent : {avg_expenses:.2f}\n")
	
def delete_expense():
	if not expenses:
		print("No expenses to delete\n")
		return
		
	delete_expense = input("Enter the category you want to delete\n").lower()
	
	if delete_expense == "":
		print("Category can't be empty\n")
		return
		
	if delete_expense in expenses:
		expenses.pop(delete_expense)
		print("Expense deleted\n")
	else:
		print("No such category exists\n")
	save_expenses()
	
def by_category():
	
	if not expenses:
		print("No expense to view\n")
		return
	
	view_expense = input("Enter the category you want to view\n").lower()
	
	if view_expense == "":
		print("Category can't be empty\n")
		return
			
	if view_expense in expenses:
		print(f"{view_expense} : ${expenses[view_expense]}\n")			
	else:
		print("No such category exist\n")
			
def highest_expense():
	if not expenses:
		print("No expenses yet\n")
		return
		
	highest_category = max(expenses, key = expenses.get)
	print("Highest expense is in: \n")
	print(f"{highest_category.upper()} : ${expenses[highest_category]}\n")

def sorted_expense():
    if not expenses:
        print("No expenses yet\n")
        return

    sorted_data = sorted(expenses.items(), key=lambda x: x[1], reverse=True)

    print("Expenses sorted by amount:\n")
    for c, a in sorted_data:
        print(f"{c.capitalize()} : ${a}")
    print()
		
while True:
	print("Choose what you want to do:\n")
	print("1. Add Expenses\n")
	print("2. View Expenses\n")
	print("3. Delete expenses\n")
	print("4. View expenses by category\n")
	print("5. Highest expense by category\n")
	print("6. View sorted expenses\n")
	print("7. Exit\n")
	
	choice = user_choice()
	
	if choice == "1":
		add_expense()
						
	elif choice == "2":
		view_expense()
		
	elif choice == "3":
		delete_expense()	
					
	elif choice == "4":
		by_category()				
		
	elif choice == "5":
		highest_expense()

	elif choice == "6":
		sorted_expense() 
							
	elif choice == "7":
		print("Have a nice day!!\n")
		break
		
	else:
		print("Use a valid Index\n")