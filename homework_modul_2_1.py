# Importing library for random and Counter
import random
from collections import Counter

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
        #Rename keys with number of dict
        common_dict[f"{key}_{i + 1}"] = value
#Create empty list
check = []
# Iterate through key, value of common_dict
for key, value in common_dict.items():
    #Add to list keys without number of dict
    check.append(key[0])

item_counts = Counter(check)
#Create empty list
correct = []
# Iterate through key, value of item_counts
for item, count in item_counts.items():
    if count > 1:
        #Add to list keys that are more than 1 time in common_dict
        correct.append(item)

# Initialize variables for helping logik
max_value = -1  # Initialize with negative infinity
key_with_max_value = None
# Initialize empty resulting dict
result_dict = {}
#Loop for all not unique keys
for i in range(len(correct)):
    # Iterate through key, value of common_dict
    for key, value in common_dict.items():
        #Check condition
        if key.startswith(correct[i]):
            #If value bigger than change max value and max key
            if value > max_value:
                max_value = value
                key_with_max_value = key
    #Add result for not unque keys to final dict
    result_dict[key_with_max_value] = value
    # Initialize variables for helping logik (to clean them)
    max_value = -1  # Initialize with negative
    key_with_max_value = None
# Iterate through key, value of common_dict
for key, value in common_dict.items():
    if key[0] not in correct:
        #Add unique keys to final dict
        result_dict[key[0]] = value

# Print resulting lists of dicts
print("list of random number of dicts:", dict_list)
print("Common Dict: ", common_dict) # only to check
print("Result Dict: ", result_dict)




