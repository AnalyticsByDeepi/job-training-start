# Name: Deepika.M
# Date: 25-06-2026
# Module 2: Core Fundamentals

# --- Task 1 ---
# Matrix Slicing and List Manipulation

data_stream = list(range(21))

# Even numbers in reverse order
reverse_even = data_stream[-1::-2]

# Middle five elements
middle_five = data_stream[8:13]

# Slice assignment
data_stream[2:4] = ["MODIFIED", "MODIFIED"]

# Append and insert
data_stream.append(99)
data_stream.insert(0, 0.5)

print("\n--- Task 1 ---")
print("Reverse Even Numbers:", reverse_even)
print("Middle Five Elements:", middle_five)
print("Final List:", data_stream)
print("Length of Final List:", len(data_stream))


# --- Task 2 ---
# Immutable Records & Tuple Unpacking

employee_record = (101, "Alice Smith", "Data Engineer", "London")

emp_id, name, role, location = employee_record

large_tuple = (10, 20, 30, 40, 50, 60)

head, *mid, tail = large_tuple

# employee_record[3] = "Paris"
# TypeError: 'tuple' object does not support item assignment

print("\n--- Task 2 ---")
print("Employee Record:", employee_record)
print("Employee ID:", emp_id)
print("Name:", name)
print("Role:", role)
print("Location:", location)

print("Head:", head)
print("Mid:", mid)
print("Tail:", tail)


## --- Task 3 ---
# Deduplication and Set Hashability

raw_ids = [1001, 1002, 1001, 1005, 1003, 1002, 1008]

unique_ids = set(raw_ids)

# unique_ids.add([1, 2])
# TypeError: unhashable type: 'list'
# Lists are mutable and cannot be stored in a set.

unique_ids.add(1009)
unique_ids.update([1010, 1011])

print("\n--- Task 3 ---")
print("Unique IDs:", unique_ids)
print("Total Unique IDs:", len(unique_ids))


# --- Task 4 ---
# Mathematical Set Operations

frontend_devs = {"HTML", "CSS", "JS", "React", "Python"}
backend_devs = {"Python", "Java", "NodeJS", "Go", "JS"}

full_stack = frontend_devs | backend_devs
overlap = frontend_devs & backend_devs
specialists = backend_devs - frontend_devs
unique_to_one = frontend_devs ^ backend_devs

print("\n--- Task 4 ---")
print("Union (Full Stack Skills):", full_stack)
print("Intersection (Common Skills):", overlap)
print("Difference (Backend Only):", specialists)
print("Symmetric Difference:", unique_to_one)


## --- Task 5 ---
# Collection Conversion Pipeline

float_tuple = (4.5, 2.1, 8.7, 1.3, 6.9)

float_list = list(float_tuple)
float_list.sort()

float_set = set(float_list)

size_before = len(float_set)
float_set.add(4.5)
size_after = len(float_set)

final_tuple = tuple(float_set)

print("\n--- Task 5 ---")
print("Original Tuple:", float_tuple)
print("Sorted List:", float_list)
print("Set:", float_set)
print("Size Before Duplicate Add:", size_before)
print("Size After Duplicate Add:", size_after)
print("Final Tuple:", final_tuple)

print("List Memory Address:", id(float_list))
print("Set Memory Address:", id(float_set))