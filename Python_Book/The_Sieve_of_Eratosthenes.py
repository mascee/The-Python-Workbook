# Exercise 135. The Sieve of Eratosthenes.
# This program finds all prime numbers

limit = int(input("Enter a number and I will find all primes withn this limit: "))

nums = []
for i in range(0, limit + 1):
    nums.append(i)
    i+=1
#print(nums)

#Cross out 1 by replacing it with 0
nums[1] = 0

#Set p equal to 2
p = 2
#While p is less than the limit do:
while p < limit:
    #Cross out all the multiples of p, but not p itself
    for i in range(p+2, limit +1, p):
        nums[i] = 0
    #Set p equal to the next number that is not crossed out
    p += 1
    while p < limit and nums[p] == 0:
        p += 1

print(f"The prime numbers up to {limit} are: ")
for i in nums:
    if nums[i] != 0:
        print(i)
