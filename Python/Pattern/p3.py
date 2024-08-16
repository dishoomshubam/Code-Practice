'''
1
12
123
1234
'''

row = 4


for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
        
    print()
    
    
    # Define the number of rows
rows = 3

# Loop through each row
for i in range(1, rows + 1):
    # Loop to print numbers from 1 to the current row number
    for j in range(1, i + 1):
        print(j, end=" ")
    # Print a new line after each row
    print()
