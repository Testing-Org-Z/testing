# Documentation

## Description

This code is an implementation of a solution to a problem. It takes input values and performs certain operations on them until a specific condition is met. The code calculates the minimum number of operations needed to transform the given input array into another array that satisfies a given condition.

## Input

The code expects the following input:

- The variable `t` as an integer. It represents the number of test cases.
- For each test case, two integers `n` and `J` are provided on a new line. `n` represents the size of the array and `J` is the target sum.
- On the next line, `n` space-separated integers are given, representing the elements of the array.

## Output

The code produces the following output:

- For each test case, it prints an integer representing the minimum number of operations needed to transform the array. If it is not possible to reach the target sum, it prints `-1`.

## Code Logic

1. Read the number of test cases `t` from the input.
2. Iterate `t` times to process each test case.
3. For each test case:
    a. Read the values of `n` and `J` from the input.
    b. Read `n` space-separated integers and store them in the variable `row`.
    c. Create a reversed copy of `row` and store it in the variable `frow`.
    d. Initialize a variable `op` to keep track of the number of operations.
    e. Check if the sum of elements in `row` is less than `J`. If true, print `-1` and move to the next test case.
    f. Enter a loop that executes until the sum of elements in `row` is equal to `J`.
        - If the sum of elements in `row` is equal to `J`, print the value of `op` and break the loop.
        - If the first element of `row` is equal to the first element of `frow`, find the maximum index `i` such that the subarrays `row[0:i+1]` and `frow[0:i+1]` are equal.
            - If the `i`-th element of `row` is `1`, remove the first element from `row` and the last element from `frow`.
            - If the `i`-th element of `frow` is `1`, remove the first element from `frow` and the last element from `row`.
        - If the first elements of `row` and `frow` are different, remove the first element from the array that contains `1` as its first element.
        - Increment `op` by `1`.
4. End of the program.