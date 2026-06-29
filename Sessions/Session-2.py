# Name: Deepika.M
# Date: 24-06-2026
# Module 2: Core Fundamentals

# Task 1

# Practice:
# id()
# type()
# is vs ==
# None
x = 256
y = 256

a = 257
b = 257

is_same_identity = a is b
is_same_value = a == b

status = None

print(
    f"id(x): {id(x)}\n"
    f"id(y): {id(y)}\n"
    f"id(a): {id(a)}\n"
    f"id(b): {id(b)}\n"
    f"is_same_identity: {is_same_identity}\n"
    f"is_same_value: {is_same_value}\n"
    f"type(status): {type(status)}\n"
    f"id(status): {id(status)}"
)


#Task 2

# 1. User input + 2. type casting
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = int(input("Enter hours worked: "))
tax_bracket = float(input("Enter tax bracket (e.g., 0.2 for 20%): "))

# 3. Calculation
gross_pay = hourly_rate * hours_worked
tax_amount = gross_pay * tax_bracket
net_pay = gross_pay - tax_amount

# 4. Output results
print("\n--- Payroll Summary ---")
print("Gross Pay:", gross_pay)
print("Tax Amount:", tax_amount)
print("Net Pay:", net_pay)

# 4. Validation (type checking)
print("\n--- Type Check ---")
print("hourly_rate:", type(hourly_rate))
print("hours_worked:", type(hours_worked))
print("tax_bracket:", type(tax_bracket))
print("gross_pay:", type(gross_pay))
print("net_pay:", type(net_pay))

#Task 3

# Input + casting
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = int(input("Enter hours worked: "))
tax_bracket = float(input("Enter tax bracket (e.g., 0.2 for 20%): "))

# Calculations
gross_pay = hourly_rate * hours_worked
net_pay = gross_pay - (gross_pay * tax_bracket)

# Header width
width = 40

# Header (centered with '=')
print("=" * width)
print(f"{'OFFICIAL PAYSLIP':=^{width}}")
print("=" * width)

# Salary details
print(f"{'Hourly Rate:':<25} ₹{hourly_rate:>10.3f}")
print(f"{'Hours Worked:':<25} ₹{hours_worked:>10.3f}")
print(f"{'Gross Pay:':<25} ₹{gross_pay:>10.3f}")
print(f"{'Tax Rate:':<25} ₹{tax_bracket:>10.3f}")
print(f"{'Net Pay:':<25} ₹{net_pay:>10.3f}")

# Footer divider
print("=" * width)

#Task 4
# Task 4

a = 10
b = 5
c = 2
d = 3
e = 2
f = 8
g = 3

result = ((a + b * c) / (d ** e)) - f or g

is_valid = (result > 0) and (result is not None)

print(f"Result: {result}")
print(f"is_valid: {is_valid}")

#Task 5

# 1. Define flags
GUEST = 1        # 0001
USER = 2         # 0010
ADMIN = 4        # 0100
SUPERUSER = 8    # 1000

# 2. Combine GUEST and USER using OR
current_access = GUEST | USER   # 0001 | 0010 = 0011

# 3. Elevate ADMIN using LEFT SHIFT
NEW_SECURE_LEVEL = ADMIN << 1   # 0100 << 1 = 1000 (8 -> 16 in decimal logic shift)

# 4. Check if USER bit is present using AND
has_user = current_access & USER

# 5. Toggle (remove GUEST using XOR)
current_access_toggled = current_access ^ GUEST

# 6. Print results (decimal + binary)

print("=== PERMISSION SYSTEM ===\n")

print(f"GUEST          : {GUEST}   -> {bin(GUEST)}")
print(f"USER           : {USER}   -> {bin(USER)}")
print(f"ADMIN          : {ADMIN}   -> {bin(ADMIN)}")
print(f"SUPERUSER      : {SUPERUSER}   -> {bin(SUPERUSER)}")

print("\n--- Combined Access ---")
print(f"current_access : {current_access} -> {bin(current_access)}")

print("\n--- Elevation ---")
print(f"NEW_SECURE_LEVEL : {NEW_SECURE_LEVEL} -> {bin(NEW_SECURE_LEVEL)}")

print("\n--- Check USER Bit ---")
print(f"has_user (AND)   : {has_user} -> {bin(has_user)}")

print("\n--- Toggle GUEST ---")
print(f"toggled access   : {current_access_toggled} -> {bin(current_access_toggled)}")