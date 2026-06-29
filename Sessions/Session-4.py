"""
Name: Deepika
Training ID: Your_Training_ID
Module: Python Session - 4
Date: 27-06-2026
"""

print("-" * 10 + " Task 1 " + "-" * 10)

# Task 1: The "Safe Lookup" Dictionary Engine

inventory = {
    "sku_01": 50,
    "sku_02": 150,
    "sku_03": 75
}

# Add new item
inventory.update({"sku_04": 200})

# Retrieve using bracket notation
print("Stock of sku_02:", inventory["sku_02"])

# Safe lookup using get()
print("Stock of sku_05:", inventory.get("sku_05", 0))

# Print keys and values
print("Product IDs:", list(inventory.keys()))
print("Stock Counts:", list(inventory.values()))

# Dictionary as list of tuples
print("Inventory Items:", list(inventory.items()))

print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

# Task 2: Nested JSON-like Structure

api_response = {
    "status": "success",
    "data": [
        {
            "id": 1,
            "info": {
                "email": "user1@work.com",
                "tags": ["admin", "dev"]
            }
        },
        {
            "id": 2,
            "info": {
                "email": "user2@work.com",
                "tags": ["guest"]
            }
        }
    ]
}

# Access values
user_1_email = api_response["data"][0]["info"]["email"]
user_1_secondary_tag = api_response["data"][0]["info"]["tags"][1]
last_user_id = api_response["data"][-1]["id"]

print("First User Email:", user_1_email)
print("First User Second Tag:", user_1_secondary_tag)
print("Last User ID:", last_user_id)

print("Type of data:", type(api_response["data"]))
print("Type of info:", type(api_response["data"][0]["info"]))

print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

# Task 3: String Sanitization

raw_log = " ERROR_CODE: 404 | STATUS: NOT_FOUND | SOURCE: SERVER_01 "

cleaned_log = raw_log.strip()
cleaned_log = cleaned_log.replace("_", " ")
pipe_index = cleaned_log.find("|")
cleaned_log = cleaned_log.lower()

print("Index of first | :", pipe_index)
print("Cleaned Log:")
print(cleaned_log)

print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

# Task 4: CSV Parser

csv_data = "Apple,iPhone,1200,Silver"

product_details = csv_data.split(",")

# Change price
product_details[2] = "1300"

# Join with semicolon
new_csv = ";".join(product_details)

# Header
header = "BRAND;MODEL;PRICE;COLOR"

final_output = header + "\n" + new_csv

print(final_output)

print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

# Task 5: Dictionary Merge & Pop

personal_info = {
    "name": "John",
    "age": 30
}

job_info = {
    "salary": 5000,
    "role": "Analyst"
}

# Merge dictionaries
full_profile = personal_info | job_info

print("Merged Dictionary:", full_profile)

# Remove age
removed_age = full_profile.pop("age")

print("Removed Age:", removed_age)
print("Updated Profile:", full_profile)

# Clear dictionary
personal_info.clear()

print("Length of personal_info:", len(personal_info))