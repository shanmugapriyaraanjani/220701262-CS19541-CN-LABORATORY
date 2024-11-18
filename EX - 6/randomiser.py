import random

# Function to check if a number is a power of two
def is_power_of_two(n):
    return (n != 0) and (n & (n - 1) == 0)

# Read the list from the file dynamically
with open('Code.txt', 'r') as file:
    content = file.read()

# Convert the file content into a list (assuming the content is in a list-like format)
my_list = [int(x) for x in content.strip().strip('[]').split(',')]

# Get a list of valid indices (not powers of two)
valid_indices = [i for i in range(len(my_list)) if not is_power_of_two(i)]

# Select a random valid index
random_index = random.choice(valid_indices)

# Change the element at the random index (e.g., flip the value)
my_list[random_index] = 1 if my_list[random_index] == 0 else 0

# Write the modified list back to the file
with open('Code.txt', 'w') as file:
    file.write(str(my_list))

print("Modified list written back to the file.")
