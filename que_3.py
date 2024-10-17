'''
1. Function Definition: Define the function that calculates the bitwise AND for a given range.
2. Initialize Result: Start with ans set to the value of left.
3. Loop Through Range: Iterate from left + 1 to right, performing bitwise AND with each subsequent number.
4. Return Result: After completing the loop, return the final result of the bitwise AND calculations.
5. Test Cases Definition: Create a list of tuples that define the ranges to test.
6. Loop Through Test Cases: Iterate over each tuple of test cases.
7. Print Results: For each test case, print the result of the range_bitwise_and function.

Time Complexity:
 O(n)
'''


def range_bitwise_and(left, right):
    ans = left
    for i in range(left + 1, right + 1):
        ans &= i
    return ans

test_cases = [
    (5, 7),      
    (0, 0),      
    (1, 2147483647)  
]


for left, right in test_cases:
    print(range_bitwise_and(left, right))
