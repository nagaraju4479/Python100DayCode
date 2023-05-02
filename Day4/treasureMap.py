#Treasure Map
from PIL import Image
row1 = ["🙂","🙂","🙂"]
row2 = ["🙂","🙂","🙂"]
row3 = ["🙂","🙂","🙂"]

grid = [row1,row2,row3 ]

print(f"{row1}\n{row2}\n{row3}")

row_num = int(input("Enter the row number (1-3): "))

col_num = int(input("Enter the column number (1-3): "))

# # Update the grid
# grid[row_num - 1][col_num - 1] = "X"

horizontal_row=grid[row_num - 1]
horizontal_row[col_num - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

