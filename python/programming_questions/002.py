'''
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two
 terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.

Solution:
Dave Cuthbert copyright 2017
License MIT
'''

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def solve_problem(maximum):
    fib_series =  fibonacci()
    even_sum = 0

    for f in fib_series:
        if (f % 2 == 0):
            even_sum += f
        if (f > maximum):
            break

        
    return even_sum


if __name__ == "__main__":
    MAX_VALUE = 4000000

    print(solve_problem(MAX_VALUE))
