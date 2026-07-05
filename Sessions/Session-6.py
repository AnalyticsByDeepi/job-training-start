# -----------------------------------------
# Name: Deepika M
# Date: 05-07-2026
# Task: Secure Data Scrubber
# -----------------------------------------

# ==========================
# Task - 1
# The Secure Data Scrubber
# ==========================

print("===== Task - 1 =====")

user_data = "Alpha_User 101! #Beta$ & Gamma_99"

cleaned_data = ""

for character in user_data:
    if character.isalpha():
        cleaned_data += character
    elif character == " ":
        pass
        cleaned_data += character

print("Original String :", user_data)
print("Cleaned String  :", cleaned_data)

# ==========================
# Task - 2
# Financial Threshold Monitor
# ==========================

print("===== Task - 2 =====")

prices = [120.5, 118.2, 122.0, 115.5, 125.0]

starting_price = prices[0]

for index, price in enumerate(prices[1:], start=1):
    percentage_change = ((price - starting_price) / starting_price) * 100

    print(f"Index {index}: Price = {price}, Change = {percentage_change:.2f}%")

    if percentage_change < -5:
        print(f"SELL ALERT at index {index}")

       
# ==========================
# Task - 3
# API Response Validator
# ==========================

print("===== Task - 3 =====")

service_status = {
    "Auth": "200 OK",
    "Cache": "500 Error",
    "Database": "200 OK",
    "Proxy": "404 Not Found"
}

for service, status in service_status.items():

    print(f"\nService : {service}")
    print(f"Status  : {status}")

    if "200" in status:
        print("Service Healthy")
    else:
        print("Service Critical")
        continue

    print("Logging service information...")

# ==========================
# Task - 4
# Smart Search Optimizer
# ==========================

import random

print("===== Task - 4 =====")

# Generate a list of 20 random integers
numbers = []

for _ in range(20):
    numbers.append(random.randint(1, 100))

print("Random List :", numbers)

target_id = int(input("Enter the value to search: "))

found = False

for index, value in enumerate(numbers):
    print(f"Analyzing index {index}...")

    if value == target_id:
        print(f"Target {target_id} found at index {index}.")
        found = True
        break

if found:
    print("Search was efficient (stopped before checking all elements).")
else:
    print(f"Target {target_id} not found.")
    print("Search was exhaustive (checked every element).")

# ==========================
# Task - 5
# Infinite Command-Line Interface
# ==========================

print("===== Task - 5 =====")

while True:

    command = input("Enter command (status/reset/exit): ").lower()

    match command:

        case "status":
            print("System Status: Running Successfully.")

        case "reset":
            print("System Reset Completed.")

        case "exit":
            print("Exiting the program...")
            break

        case _:
            print("Invalid command! Please enter status, reset, or exit.")


# ==========================
# Task - 6
# Multi-Dimensional Grid Mapper
# ==========================

print("===== Task - 6 =====")

for row in range(5):
    for col in range(5):

        if row == 2 and col == 2:
            continue

        print(f"({row}, {col})")


# ==========================
# Task - 7
# Resource Management Simulator
# ==========================

print("===== Task - 7 =====")

battery = 0

while battery <= 100:

    battery += 5
    print(f"Battery Level: {battery}%")

    if battery in (20, 40, 60):
        print("Charging...")

    elif battery == 80:
        pass      # Placeholder for Slow Charge Mode
        print("Battery Level: 80%")

    elif battery == 100:
        print("Fully Charged")
        break        


# ==========================
# Task - 8
# The "Dirty Data" Integrator
# ==========================

# A for loop is used to process each sensor reading one by one.
# continue skips invalid data, while break stops processing when a critical error occurs.

print("===== Task - 8 =====")

logs = [22, 25, "TIMEOUT", 28, 0, "ERROR", 30]

total_temperature = 0
count = 0

for reading in logs:

    if reading == "TIMEOUT":
        print("TIMEOUT detected - Skipping reading.")
        continue

    if reading == 0:
        print("False reading (0) - Ignoring.")
        continue

    if reading == "ERROR":
        print("ERROR detected - Stopping data processing.")
        break

    total_temperature += reading
    count += 1

if count > 0:
    average = total_temperature / count
    print(f"\nTotal Temperature : {total_temperature}")
    print(f"Valid Readings    : {count}")
    print(f"Average Temperature: {average:.2f}")
else:
    print("No valid temperature data available.")


# ==========================
# Task - 9
# The Prime Number Architect
# ==========================

# A nested loop is used to test each number for factors.
# The break statement stops checking as soon as a factor is found, making the loop more efficient.

print("===== Task - 9 =====")

print("Prime Numbers from 2 to 50:")

for number in range(2, 51):

    is_prime = True

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
print()


# ==========================
# Task - 10
# State-Machine Transaction Logic
# ==========================

# A while loop allows the user to make multiple purchases until they finish or the balance is exhausted.
# continue lets the user retry unaffordable items, break ends the loop, and pass acts as a placeholder for future refund logic.

print("===== Task - 10 =====")

balance = 50

items = {
    "Soda": 15,
    "Chips": 10,
    "Candy": 5
}

while True:

    print(f"\nAvailable Balance: ₹{balance}")
    print("Items Available:")

    for item, price in items.items():
        print(f"{item} - ₹{price}")

    choice = input("\nEnter an item to buy (or type 'finished'): ").title()

    if choice.lower() == "finished":
        print("Transaction Finished.")

        # Placeholder for future refund feature
        pass

        break

    if choice not in items:
        print("Invalid item. Please choose a valid item.")
        continue

    if items[choice] > balance:
        print("Insufficient balance! Please choose another item.")
        continue

    balance -= items[choice]

    print(f"{choice} purchased successfully.")
    print(f"Remaining Balance: ₹{balance}")

    if balance == 0:
        print("Balance is zero. Transaction ended.")
        break