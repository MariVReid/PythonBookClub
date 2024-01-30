# top of your program
import timeit
import math
import numpy

# user input
start_time = timeit.default_timer()
# number crunching and such
prime_numbers = [2, 3, 5, 7]
num = 10
division = list(range(2, 15))
while len(prime_numbers) < 100:
    remainders = []
    for value in division:
        remainders.append(num % value)
    if numpy.prod(remainders) != 0:
        prime_numbers.append(num)
    num += 1
print(prime_numbers)
# print results and end of program
stop_time = timeit.default_timer()
print('Runtime (seconds): ', stop_time - start_time)
print('\nLength of prime_numbers"', len(prime_numbers))