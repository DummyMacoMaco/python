"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.

input: integer
output: true iff palindrome, false otherwise
"""

class Solution:
	def isPalindrome(self, x: int):
		# forAll condition
		palindrome = True
		numberString = str(x)
		left = 0
		right = len(numberString) - 1
		while (left < right and palindrome):
			palindrome = numberString[left] == numberString[right]
			left += 1
			right -= 1

		return palindrome

solution = Solution()
print(solution.isPalindrome(121) == True)
print(solution.isPalindrome(-121) == False)
print(solution.isPalindrome(10) == False)
print(solution.isPalindrome(111) == True)