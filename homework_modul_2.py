# Importing library for random
import random

# Create a list of random number of dicts (from 2 to 10)
# Create empty list
dict_list = []
# Generate a random number of dicts between 2 and 10
num_d = random.randint(2, 10)

# Generate random dicts and append them to the list
# Cycle from 0 to num_d - 1
for i in range(num_d):
# Generate a random number of pairs (between 1 and 10)
    num_key = random.randint(1, 10)
# Create empty dict
    dict_i = {}
# Cycle from 0 to num_key - 1
    for j in range(num_key):
# Generate a random lowercase letter
        key = chr(random.randint(97, 122))
# Generate a random int number from 0 to 100
        value = random.randint(0, 100)
# Add key and value in dict
        dict_i[key] = value
# Add dict to dict list
    dict_list.append(dict_i)

# Get previously generated list of dicts and create one common dict
common_dict = {}

# Iterate through the list of dicts
for i, j in enumerate(dict_list):
# Iterate through the key-value pairs in each dict
    for key, value in j.items():
# If the key is not in the common_dict, add it as is
        if key not in common_dict:
            common_dict[key] = value
        else:
# If the key is already in common_dict, update it with the max value
            if value > common_dict[key]:
# Delete previuos key, value
                del common_dict[key]
                common_dict[key] = value

# Print resulting lists of dicts
print("list of random number of dicts:", dict_list)
print("Common Dict: ", common_dict)

