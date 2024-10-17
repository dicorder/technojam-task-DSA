'''

1. Initialize the result: Start with the left endpoint of the range.

2. Iterate through the range: Loop from one more than left to right, inclusive.
3. Bitwise AND operation: Update the result with the bitwise AND of the current number in the loop.
4. Return the result: Finally, return the accumulated result after all iterations.


Time Complexity:𝑂(𝑛) 
'''


def climb_stairs(n):
    if n <= 1:
        return 1

    first = 1
    second = 1

    for i in range(2, n + 1):
        current = first + second
        first = second
        second = current

    return second

if __name__ == "__main__":
    n = 2
    print(climb_stairs(n)) 
