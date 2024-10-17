'''
1. Initialize Triangle: Create an empty list to store the rows of Pascal's Triangle.
2. Iterate Rows: Loop through the number of rows to generate each row.
3. Row Initialization: Start each row with 1s to set the edges of the triangle.
4. Fill Inner Elements: For rows greater than 1, calculate the inner elements using values from the previous row.
5. Append Row: Add the completed row to the main triangle list.
6. Print Rows: Output each row of the triangle after it has been fully constructed.
7. Main Function: Define the number of rows and call the function to generate and print the triangle.

Time Complexity:O(n^2)
'''


def generate_pascal_triangle(n):
    triangle = []

    for row in range(n):
        
        current_row = [1] * (row + 1)
        
        
        for col in range(1, row):
            current_row[col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
        
        triangle.append(current_row)

    
    for row in triangle:
        print(row)

if __name__ == "__main__":
    n = 5
    generate_pascal_triangle(n)
