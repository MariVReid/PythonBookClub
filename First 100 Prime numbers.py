#A Program to list the first 100 Prime numbers
x=0
#count=1
number=3
primes = [2]
extent = 100000 #modify to switch the number of primes reported
while len(primes)<extent: 
    x=0
    #if number==2:
     #   print(f"2 is prime number 1")
      #  count=count+1
       # number=number+1
        #continue
    if number%2 ==0 or number%3==0 or number%5==0 or number%7==0:
        #print("I detected an even number")
        number=number+1
    else:
        bHalf=int((number+1)/2)
        #print(bHalf)
        for  num in range(3, bHalf+1,2):
            print(f"The number I am working on is {number}")
            if number%num==0:
                number=number+1
                x=1
                break
        if x!= 1:
            primes.append(number)
            #count=count+1
            number=number+1
print(f"The first {extent} prime numbers are:\n")
print(primes)
            
## to do add numbers into array and print at the end                 