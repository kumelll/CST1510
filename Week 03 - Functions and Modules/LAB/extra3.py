
from datetime import datetime

username = input("Enter username: ")
action = input("Enter action (LOGIN or LOGOUT): ").upper()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"[{timestamp}] {action} user={username}")
