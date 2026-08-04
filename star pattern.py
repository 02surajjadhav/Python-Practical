rows=int(input("Enter Rows:"))
for i in range(1, rows+1):
    print("*" * i)
    
for i in range(rows, 0, -1):
    print("*" * i)
    
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))
for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, rows + 1):
    for j in range(i):
        print(i, end=" ")
    print()

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
