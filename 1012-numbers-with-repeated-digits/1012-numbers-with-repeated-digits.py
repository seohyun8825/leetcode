from math import factorial
from typing import List
##bb
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_digits(limit: int) -> int:
            digits = list(map(int, str(limit + 1)))
            length = len(digits)


            unique_count = 0

            for i in range(1, length):
                unique_count += 9 * permutations(9, i - 1)
            
            seen = set()
            for i in range(length):
                for x in range(1 if i == 0 else 0, digits[i]):
                    if x in seen:
                        continue
                    unique_count += permutations(9 - i, length - i - 1)
                if digits[i] in seen:
                    break
                seen.add(digits[i])
            
            return unique_count
        
        def permutations(m: int, k: int) -> int:

            if k > m:
                return 0
            return factorial(m) // factorial(m - k)

        total_count = n
        unique_count = count_unique_digits(n)
        return total_count - unique_count
