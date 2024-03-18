class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n < 2 or n % 2 == 1:
            z = n * 2
        elif n == 2:
            z = 2
        elif n > 2 and n % 2 != 1:
            z = n
        return(z)
