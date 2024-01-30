#A Program to list the first X Prime numbers
import math
import timeit

start_time = timeit.default_timer()

x=0
number=3
primes = [2]
extent = 100000 #modify to switch the number of primes reported
while len(primes)<extent: 
    x=0
    if number%2 ==0:
        number=number+1
    else:
        for num in primes:
            if num > math.sqrt(number):
                break
            elif number%num==0:
                number=number+1
                x=1
                break
        if x!= 1:
            primes.append(number)
            number=number+1
#print(f"\nThe first {extent} prime numbers are:\n")
print(primes)
            
stop_time = timeit.default_timer()
print('Runtime (seconds): ', stop_time - start_time)  
             