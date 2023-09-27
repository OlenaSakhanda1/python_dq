# Importing library for random and Counter
import random
from collections import Counter

def generate_dict_list(num_d):
    dict_list = []
    for i in range(num_d):
        num_key = random.randint(1, 10)
        dict_i = {}
        for j in range(num_key):
            key = chr(random.randint(97, 122))
            value = random.randint(0, 100)
            dict_i[key] = value
        dict_list.append(dict_i)
    return dict_list

def generate_common_dict(dict_list):
    common_dict = {}
    for i, j in enumerate(dict_list):
        for key, value in j.items():
            common_dict[f"{key}_{i + 1}"] = value
    return common_dict

def generate_result_dict(common_dict):
    check = []
    for key, value in common_dict.items():
        check.append(key[0])

    item_counts = Counter(check)
    correct = []
    for item, count in item_counts.items():
        if count > 1:
            correct.append(item)

    max_value = -1
    key_with_max_value = None
    result_dict = {}
    for i in range(len(correct)):
        for key, value in common_dict.items():
            if key.startswith(correct[i]):
                if value > max_value:
                    max_value = value
                    key_with_max_value = key
        result_dict[key_with_max_value] = max_value
        max_value = -1
        key_with_max_value = None
    for key, value in common_dict.items():
        if key[0] not in correct:
            result_dict[key[0]] = value
    return result_dict

num_d = random.randint(2, 10)
dict_list = generate_dict_list(num_d)
common_dict = generate_common_dict(dict_list)
result_dict = generate_result_dict(common_dict)

print("list of random number of dicts:", dict_list)
print("Common Dict: ", common_dict)
print("Result Dict: ", result_dict)




