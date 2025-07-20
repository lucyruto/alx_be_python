# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop to handle rows
while row < size:
    # Inner for loop to handle columns
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1
