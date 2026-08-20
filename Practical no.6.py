print("========================================")
print("        INVOICE & RECEIPT GENERATOR")
print("========================================")
print("\n--- EXERCISE 1: RECEIPT NUMBER PATTERN ---")

rows_pattern = int(input("Enter number of rows for receipt pattern: "))

print("\nGenerated Pattern:")

for i in range(1, rows_pattern + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

print("\n" + "-" * 40)
print("--- EXERCISE 2: INVOICE FRAME BORDER ---")

frame_rows = int(input("Enter frame height (rows): "))
frame_cols = int(input("Enter frame width (columns): "))

print("\nGenerated Border:")

for i in range(frame_rows):
    for j in range(frame_cols):
        if i == 0 or i == frame_rows - 1 or j == 0 or j == frame_cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
