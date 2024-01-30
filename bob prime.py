# Find all prime numbers from 2 to max...

# Imports...

import timeit



print("Howdy! This program will identify all prime\nnumbers from 1 to a user-defined maximum.\n")

max_dividend = int(input("   Enter the maximum (an integer) of the search range: "))



primes = [2]

current_dividend = 3

start = timeit.default_timer()



while(current_dividend <= max_dividend):

	#print(f"Checking {current_dividend}")

	current_divisor = 3

	is_prime_flag = True

	while((current_divisor <= (int(current_dividend/2))) and (is_prime_flag == True)):

		#print(f"Checking divisor = {current_divisor}")

		if(current_dividend % current_divisor == 0):

			is_prime_flag = False

			break

		current_divisor += 2

	# Well, was it prime?

	if(is_prime_flag == True):

		#print("Yep!")

		primes.append(current_dividend)

	#else:

		#print("Nope!")

	current_dividend += 2



# Print the prime numbers...

number_of_primes = len(primes)

print(f"\nThere are {number_of_primes} prime numbers between 1 and {max_dividend}:")

print(primes)



# We're done...

stop = timeit.default_timer()

print('\nRuntime (in seconds): ', stop - start)

print("\n\n") 