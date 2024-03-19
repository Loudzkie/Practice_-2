def character_frequency_counter(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

# Sample Input
input_string = input("Enter a string: ")

# Calculate character frequency
frequency = character_frequency_counter(input_string)

# Print the result
print("Character frequency:")
for char, count in frequency.items():
    print(f"{char}: {count}")
