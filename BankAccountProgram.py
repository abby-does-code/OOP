# This program demonstrates the BankAccount class.

import BankAccountClass


def main():

    # Get the starting balance.
    start_bal = float(input("Enter your starting balance: "))

    # Create a BankAccount object.
    ##Creating an instance based on the BankAccountClass and we HAVE to give it a variable
    ##If it was left blank, you'd have an error
    savings = BankAccountClass.BankAccount(start_bal)

    # Deposit the user's paycheck.
    pay = float(input("How much were you paid this week? "))
    print("I will deposit that into your account.")
    ##This calls the deposit method
    ##Use the "pay" to call the method and used as the amount argument in the method
    savings.deposit(pay)

    # Display the balance.
    ##Calls the method "get balance"
    print("Your account balance is $", format(savings.get_balance(), ",.2f"), sep="")

    # Get the amount to withdraw.
    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account.")
    ##Calls the withdraw method
    savings.withdraw(cash)

    # Display the balance.
    print("Your account balance is $", format(savings.get_balance(), ",.2f"), sep="")


# Call the main function.
main()
