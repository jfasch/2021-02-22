import sys


prime_candidate = input('Enter number to check for primeness: ')
try:
    prime_candidate = int(prime_candidate)
except ValueError:
    print('You idiot:', prime_candidate, 'is not a number')
    sys.exit()

# low hanging fruit: 1 is not prime
if prime_candidate == 1:
    print(prime_candidate, 'is not prime')
    sys.exit()

divisor = 2
while divisor < prime_candidate / 2:
    if prime_candidate % divisor == 0:
        print(prime_candidate, 'is not prime')
        break
    divisor += 1
else:
    print(prime_candidate, 'is prime')
