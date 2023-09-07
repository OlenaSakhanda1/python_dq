# Importing library for random
import random

# Create a list of 100 random numbers from 0 to 1000
# Create empty array
list100 = []
# Cycle from 0 to 99
for i in range(100):
# Add to list100 next int random number from 0 to 1000
    list100.append(random.randint(0,1000))

# Sort the list without using the sort() method
# Initialize variable n that is equal 100
n = 100
# Cycle from 0 to 99
for i in range(n):
# Initialize variable min_ind that is equal i
    min_ind = i
# Cycle from i+1 to 99
    for j in range(i+1, n):
# Check condition element < min element
        if list100[j] < list100[min_ind]:
# If condition true than min_ind = new min element index
            min_ind = j
# Change element i with min element
    list100[i], list100[min_ind] = list100[min_ind], list100[i]

# Calculate the average for even and odd numbers
# Initialize variables to calculate the sum and count of even and odd numbers
sum_even, count_even, sum_odd, count_odd = 0, 0, 0, 0
# Cycle for all elements in array
for number in list100:
# Check condition element is even or not
    if number % 2 == 0:
# Change sum for even elements
        sum_even += number
# Change count for even elements
        count_even += 1
# If element is not even
    else:
# Change sum for odd elements
        sum_odd += number
# Change count for odd elements
        count_odd += 1

# Check condition count of even elements not equal 0
if count_even > 0:
# Count average for even elements
    avg_even = sum_even / count_even
# If count of even elements equal 0 than average for even elements = 0
else: avg_even = 0
# Check condition count of odd elements not equal 0
if count_odd > 0:
# Count average for odd elements
    avg_odd = sum_odd / count_odd
# If count of odd elements equal 0 than average for odd elements = 0
else: count_odd = 0

# print both average result in console
print("Average for even numbers: ", avg_even)
print("Average for odd numbers: ", avg_odd)




