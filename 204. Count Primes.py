class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 0:
            return 0
        primes = 0
        for i in range(n):
            if self.is_prime(i):
                primes += 1
        return primes
    def is_prime(self,n):
        from math import sqrt
        prime_flag = 0
        if (n > 1):
            for i in range(2, int(sqrt(n)) + 1):
                if (n % i == 0):
                    prime_flag = 1
                    break
            if (prime_flag == 0):
                return True
            else:
                return False
        else:
            return False
print(Solution().countPrimes(10))