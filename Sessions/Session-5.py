# -----------------------------------------
# Name: Deepika.M
# Date: 29-06-2026
# File: Session-5.py
# -----------------------------------------

# ==========================
# Task - 1
# Truthy / Falsy Validation
# ==========================

print("===== Task - 1 =====")

val_1 = 0
val_2 = 0.0
val_3 = ""
val_4 = None
val_5 = "False"

if val_1:
    print(f"Variable val_1 with value {val_1} is evaluated as TRUE")
else:
    print(f"Variable val_1 with value {val_1} is evaluated as FALSE")

if val_2:
    print(f"Variable val_2 with value {val_2} is evaluated as TRUE")
else:
    print(f"Variable val_2 with value {val_2} is evaluated as FALSE")

if val_3:
    print(f"Variable val_3 with value '{val_3}' is evaluated as TRUE")
else:
    print(f"Variable val_3 with value '{val_3}' is evaluated as FALSE")

if val_4:
    print(f"Variable val_4 with value {val_4} is evaluated as TRUE")
else:
    print(f"Variable val_4 with value {val_4} is evaluated as FALSE")

if val_5:
    print(f"Variable val_5 with value '{val_5}' is evaluated as TRUE")
else:
    print(f"Variable val_5 with value '{val_5}' is evaluated as FALSE")

# Explanation:
# "False" is a non-empty string.
# In Python, every non-empty string is considered TRUE,
# regardless of its actual text.


# ==========================
# Task - 2
# Tax Engine
# ==========================

print("\n===== Task - 2 =====")

annual_income = float(input("Enter Annual Income: "))
residency_status = input("Enter Residency Status (Resident/Non-Resident): ")

if annual_income <= 30000:
    tax_rate = 0

elif annual_income <= 80000:
    if residency_status.lower() == "resident":
        tax_rate = 10
    else:
        tax_rate = 15

else:
    tax_rate = 25

tax_amount = annual_income * tax_rate / 100
remaining_balance = annual_income - tax_amount

print("\n------ Tax Summary ------")
print(f"Annual Income     : {annual_income}")
print(f"Residency Status  : {residency_status}")
print(f"Tax Rate Applied  : {tax_rate}%")
print(f"Tax Amount        : {tax_amount}")
print(f"Remaining Balance : {remaining_balance}")


# ==========================
# Task - 3
# Match Case - HTTP Status
# ==========================

print("\n===== Task - 3 =====")

status_code = int(input("Enter HTTP Status Code: "))

# match-case is used instead of switch-case.

match status_code:
    case 200:
        print("Success: OK")

    case 400:
        print("Client Error: Bad Request")

    case 404:
        print("Client Error: Not Found")

    case 500:
        print("Server Error: Internal Server Error")

    case _:
        print("Unknown Status Code")


# ==========================
# Task - 4
# File Extension Matching
# ==========================

print("\n===== Task - 4 =====")

file_ext = input("Enter File Extension: ").lower()

# Pipe operator (|) combines multiple patterns.

match file_ext:
    case ".jpg" | ".jpeg" | ".png":
        print("File Type: Image")

    case ".pdf" | ".docx" | ".txt":
        print("File Type: Document")

    case ".mp4" | ".mkv":
        print("File Type: Video")

    case _:
        print("File Type: Unsupported")


# ==========================
# Task - 5
# Short Circuit Logic
# ==========================

print("\n===== Task - 5 =====")

is_admin = input("Are you Admin? (True/False): ") == "True"
has_security_key = input("Do you have Security Key? (True/False): ") == "True"
system_offline = input("Is System Offline? (True/False): ") == "True"

if (is_admin and has_security_key) or system_offline:
    print("OVERRIDE ACCESS GRANTED")
else:
    print("ACCESS DENIED")