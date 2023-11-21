numbers = []

for i in range(5):
    numbers.append(int(input(f"Enter {i+1}th number: ")))

print("This is the list:", numbers)

sum_val = sum(numbers)
print("Sum:", sum_val)
