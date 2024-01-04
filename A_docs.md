# Igloo Index Generator

This code generates a list of igloo indices based on certain criteria and then prints the index corresponding to the given input.

## Input

The code takes an integer input `t` from the user, which represents the number of test cases. Each test case consists of an integer `k`, representing the position of the igloo index to be printed.

## Igloo Index Generation

The code first generates a list of igloo indices using a list comprehension. It loops through numbers from 0 to 1999 and only includes those numbers that satisfy the following conditions:
- The number is not divisible by 3 (i.e. `i % 3 != 0`)
- The last digit of the number is not 3 (i.e. `i % 10 != 3`)

The resulting list contains 1333 igloo indices.

## Printing Igloo Index

For each test case, the code takes an integer `k` as input. It then prints the igloo index at position `k - 1` from the generated list. Since the list is 0-indexed, we subtract 1 from `k` to get the correct index.

## Example

### Input
```
3
1
5
10
```

### Output
```
1
9
16
```

In this example, we have 3 test cases. For the first test case, the input is `1`. The code prints the igloo index at position `1 - 1 = 0`, which is `1`. Similarly, for the second test case, the input is `5`, and the code prints the igloo index at position `5 - 1 = 4`, which is `9`. Finally, for the third test case, the input is `10`, and the code prints the igloo index at position `10 - 1 = 9`, which is `16`.