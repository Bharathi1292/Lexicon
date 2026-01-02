# Global variable
balance = 10000

def account_manager():
    balance = 500  # Enclosing variable

    def transaction_manager():
        balance = 100  # Local variable

        def apply_transaction():
            nonlocal balance  
            global global_balance  
            print("Before transaction:")
            print(f"  balance (local): {balance}")
            print(f"  global_balance (global): {global_balance}")

            # Update balances
            balance += 50
            global_balance += balance

            print("After transaction:")
            print(f"  balance (local modified): {balance}")
            print(f"  global_balance (global modified): {global_balance}")

        apply_transaction()
        print(f"Back in transaction_manager, balance: {balance}")

    transaction_manager()
    print(f"Back in account_manager, balance: {balance}")


global_balance = 10000

print(f"Before account_manager: balance = {balance}, global_balance = {global_balance}\n")
account_manager()
print(f"\nAfter account_manager: balance = {balance}, global_balance = {global_balance}")
