def add_expense(expenses):
  category = input("Enter the expense category: ")
  amount = float(input("Enter the amount: "))
  expenses.append({'category': category, 'amount': amount})

def view_expenses(expenses):
  if len(expenses) == 0:
      print("No expenses recorded.")
  else:
      for expense in expenses:
          print(f"Category: {expense['category']}, Amount: {expense['amount']}")

def total_expenses(expenses):
  total = sum(expense['amount'] for expense in expenses)
  print(f"Total expenses: {total}")

def main():
  expenses = []
  while True:
      print("\n1. Add expense")
      print("2. View expenses")
      print("3. Total expenses")
      print("4. Exit")

      choice = input("Select an option (1/2/3/4): ")

      if choice == '1':
          add_expense(expenses)
      elif choice == '2':
          view_expenses(expenses)
      elif choice == '3':
          total_expenses(expenses)
      elif choice == '4':
          break
      else:
          print("Invalid choice, please try again.")

if __name__ == "__main__":
  main()
