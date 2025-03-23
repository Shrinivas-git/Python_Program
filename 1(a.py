
class Bank:
    def bank_details(self):
        print("Bank: ABC Bank")

class BankEmployee(Bank):
    def employee_details(self):
        print("Employee: John Doe")


class SavingsAccount:
    def savings_account_details(self):
        print("Savings Account: Interest Rate is 4%.")

class CurrentAccount:
    def current_account_details(self):
        print("Current Account: No Interest, Unlimited Transactions.")

class Customer(SavingsAccount, CurrentAccount):
    def customer_details(self):
        print("Customer: Alice, Account Holder.")
class Account:
    def account_details(self):
        print("Account: Generic Bank Account.")

class DepositAccount(Account):
    def deposit_details(self):
        print("Deposit Account: Minimum Balance is $500.")

class FixedDepositAccount(DepositAccount):
    def fixed_deposit_details(self):
        print("Fixed Deposit Account: Lock-in Period is 1 Year.")


class Transaction:
    def transaction_details(self):
        print("Transaction: Generic Transaction.")

class Withdrawal(Transaction):
    def withdrawal_details(self):
        print("Withdrawal: Daily Limit is $2000.")

class Deposit(Transaction):
    def deposit_details(self):
        print("Deposit: No Limit on Amount.")
class BankSystem:
    def system_details(self):
        print("Banking System: Core Banking Platform.")

class LoanSystem(BankSystem):
    def loan_system_details(self):
        print("Loan System: Handles all types of loans.")

class HybridBanking(LoanSystem, BankSystem):
    def hybrid_system_details(self):
        print("Hybrid Banking System: Integrates Loan and Banking Platforms.")


print("Single Inheritance:")
employee = BankEmployee()
employee.bank_details()
employee.employee_details()

print("\nMultiple Inheritance:")
customer = Customer()
customer.savings_account_details()
customer.current_account_details()
customer.customer_details()

print("\nMultilevel Inheritance:")
fd_account = FixedDepositAccount()
fd_account.account_details()
fd_account.deposit_details()
fd_account.fixed_deposit_details()

print("\nHierarchical Inheritance:")
withdrawal = Withdrawal()
deposit = Deposit()
withdrawal.transaction_details()
withdrawal.withdrawal_details()
deposit.transaction_details()
deposit.deposit_details()

print("\nHybrid Inheritance:")
hybrid_system = HybridBanking()
hybrid_system.system_details()
hybrid_system.loan_system_details()
hybrid_system.hybrid_system_details()