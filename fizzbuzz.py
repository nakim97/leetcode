# 412: FizzBuzz
# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of 3, it should output "fizz" instead of the number and for the multiples of five output "Buzz"
# For numbers which are multiples of both three and five output "FizzBuzz"


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lst = []
        for i in range(1,n+1):
            if i % 3 == 0:
                lst.append("Fizz")
            if i % 5 == 0:
                lst.append("Buzz")
            elif i % 15 ==0:
                lst.append("FizzBuzz")
            lst.append(str(i))
        return lst
