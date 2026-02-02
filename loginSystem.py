import time

USERNAME = "admin"
PASSWORD = "Admin@123"

MAX_ATTEMPTS = 3
LOCK_TIME = 10  # seconds

attempts = 0
locked_until = 0

while True:
    current_time = time.time()

    # Check if account is locked
    if current_time < locked_until:
        remaining = int(locked_until - current_time)
        print(f"Account locked 🔒 Try again in {remaining} seconds.\n")
        time.sleep(1)
        continue

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful ✅ Welcome!")
        break
    else:
        attempts += 1
        print("Invalid credentials ❌")

        if attempts >= MAX_ATTEMPTS:
            locked_until = time.time() + LOCK_TIME
            attempts = 0
            print(f"Too many attempts 🚫 Account locked for {LOCK_TIME} seconds.\n")
