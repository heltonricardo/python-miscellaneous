class Vault:
    def __init__(self, code):
        self.code = code
        self.is_locked = True

    def __enter__(self):
        print("Entering the vault...")
        return self

    def unlock(self, code_attempt):
        if code_attempt == self.code:
            self.is_locked = False
            print("Vault unlocked successfully!")
        else:
            print("Incorrect code. Vault remains locked.")

    def __exit__(self, exception_class, exception_value, traceback):
        if not self.is_locked:
            print("Exiting the vault...")
        else:
            print("Vault is still locked. Exiting without changes.")


print("Attempting to open the vault...")
code_attempt = input("Enter the vault code: ")

with Vault("1234") as vault:
    vault.unlock(code_attempt)

print("Vault is closed and locked.")
