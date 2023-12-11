N = int(input("Enter the value of N: "))
count = 0  # Count how many prime numbers found
num = 2  # Starting number to check for prime numbers

while count < N:
    isPrime = True  # Assuming the number is prime initially
    for i in range(2, num):
        if num % i == 0:  #if remainder equal to 0 then it's not a prime_number
            isPrime = False
            break
    else:
        print(num)
        count += 1  # Increment the prime number count
    num += 1



