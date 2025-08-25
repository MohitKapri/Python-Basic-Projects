print("----Welcome to Banking Management System----")

balance = 0

account_holder=input("Enter account holder name :")
account_number=input("Enter your account number :")
pin = "1234"  


user_pin = input("Enter your 4-digit PIN to login: ")
if user_pin != pin:
    print(" Incorrect PIN. Access Denied.")
    exit()

transaction = []

while True:
    print("----Main Menu---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5 Update Account Detail")
    print("6. Clear Transaction History")
    print("7. Exit")


    choice = input("Enter your choice (1-7) :")

    if choice == "1":
        print(f"Current Balance: Rs {balance}")

    elif choice == "2":
        deposit = int(input("Enter the amount to deposit: Rs "))
        if deposit > 0:
            balance += deposit
            transaction.append(f"Deposited Rs{deposit}")
            print(f" Rs{deposit} Deposited Successfully! ")
        else:
            print("Enter the valid amount.")

    elif choice =="3":
        withdraw = int(input("Enter the amount to withdraw: Rs"))
        if withdraw > balance:
            print("Insufficient balance! ")
        elif withdraw <= 0:
            print("Enter the valid amount")
        else:
            balance -=withdraw
            transaction.append(f"Withdrawn Rs{withdraw}")
            print(f" Rs{withdraw} Withdrawn Successfully! ")

    elif choice =="4":
        print("\n Transaction History:")
        if not transaction:
            print("No transaction yet.")
        else:
            for t in transaction:
                print("*",t)

    elif choice =="5":
        print("\n Update Transaction Detail")
        new_name = input("Enter new account holder name: ")
        new_number =input("Enter new account number: ")
        account_holder = new_name
        account_number = new_number
        print("Account Details Updated Successfully!")
        print(f"Updated Name: {account_holder}")
        print(f"Updated Number: {account_number}")

    elif choice =="6":
        confirm = input("Are you sure want to clear history? (yes/no): ")
        if confirm.lower() == "yes":
            transaction.clear()
            print("Transaction History Cleared")
        else:
            print("Cancelled.")
     
    
    elif choice =="7":
        print("Thank you for using our banking management system.")
        break
    

    else:
        print("Invalid choice, Please try again")




