def sum_of_multiples(num1, num2, limit):
    total = 0
    for i in range(1, limit):
        if i % num1 == 0 or i % num2 == 0:
            total += i
    return total

# Test the function with sample input
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
limit = int(input("Enter the limit: "))

result = sum_of_multiples(first_number, second_number, limit)
print(f"The sum of multiples of {first_number} or {second_number} up to {limit} is {result}.")
