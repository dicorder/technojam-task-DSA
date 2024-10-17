'''
Simple Maths 
There is a pattern in the number 


TC O(1) FOR SPIRAL FUNCTION

'''

def number_spiral(x, y):
    l = max(x, y) - 1
    if l % 2 == 1:
        if x < y:
            return l * l + x
        else:
            return l * l + 2 * l - y + 2
    else:
        if x < y:
            return l * l + 2 * l - x + 2
        else:
            return l * l + y



# Default Test Cases
test_cases = [
    (2, 3),  # Output: 8
    (1, 1),  # Output: 1
    (4, 2),  # Output: 15
]

# Run Test Cases
for y, x in test_cases:
    print(number_spiral(y, x))
