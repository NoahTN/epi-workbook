# https://leetcode.com/problems/count-primes/
# O(n sqrt(n)), O(n)

class Solution:
   def countPrimes(self, n: int) -> int:
      if n < 2: 
         return 0
      prime = [1] * n
      prime[0] = 0
      prime[1] = 0
      
      for i in range(2, int(sqrt(n))+1):
         if prime[i]:
            # Set all multiples of the integer to not prime
            prime[i * i: n: i] = [0] * len(prime[i * i: n: i])
      return sum(prime)
