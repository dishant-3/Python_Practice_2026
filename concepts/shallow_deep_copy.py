import copy

# A nested list: [Name, [Math Score, Science Score]]
original_list = ["Alice", [85, 90]]

# Create a shallow copy
shallow_copied_list = copy.copy(original_list)

# Verify they are different outer objects
print(original_list is shallow_copied_list)  # False (Outer shells are independent)

# --- Scenario 1: Modifying a non-nested, immutable element ---
shallow_copied_list[0] = "Bob"
print("Original:", original_list)       # ['Alice', [85, 90]]
print("Shallow:",  shallow_copied_list)  # ['Bob', [85, 90]]
# (Result: Changing 'Bob' only affected the copy. This works fine.)

# --- Scenario 2: Modifying a nested, mutable element ---
shallow_copied_list[1][0] = 99
print("Original:", original_list)       # ['Alice', [99, 90]] <-- CHANGED!
print("Shallow:",  shallow_copied_list)  # ['Bob', [99, 90]]
# (Result: Modifying the nested list inside the copy altered the original list too!)

###################################
import copy

# The same nested list
original_list = ["Alice", [85, 90]]

# Create a deep copy
deep_copied_list = copy.deepcopy(original_list)

# Verify the inner lists point to completely different memory addresses
print(original_list[1] is deep_copied_list[1])  # False (Inner lists are completely distinct)

# --- Scenario: Modifying the nested mutable element ---
deep_copied_list[1][0] = 99

print("Original:", original_list)    # ['Alice', [85, 90]] <-- Safe and untouched!
print("Deep Copy:", deep_copied_list)  # ['Alice', [99, 90]]

############################################
print("dishant code ")
original_list = ["Princeess", "Meghna"]

# Create a shallow copy
shallow_copied_list = copy.copy(original_list)

# Verify they are different outer objects
print(original_list is shallow_copied_list)  # False (Outer shells are independent)
print(f"Original memory:{id(original_list)}")
print(f"Shallow Object Memory:{id(shallow_copied_list)}")
# --- Scenario 1: Modifying a non-nested, immutable element ---
shallow_copied_list[0] = "Anil"
print("Original:", original_list)       # ["Princeess", "Meghna"]
print("Shallow:",  shallow_copied_list)  # ["Anil", "Meghna"]
