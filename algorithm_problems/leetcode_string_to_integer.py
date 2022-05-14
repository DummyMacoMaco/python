"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""

class Solution:
	def myAtoi(self, s: str):
		number = 0	# defualt value
		sign = 1 	# default sign +
		index = 0	# to move on the string
		string_len = len(s)
		# True iff found a non valid char while considering a valid string
		out = False
		# True iff considering a valid string to convert into integer
		in_between = False
		while (index < string_len and not out):
			# converting in ASCII
			c = ord(s[index])
			if c == 32: # ' '
				# if already read a number-char is time to end
				if in_between:
					out = True
			elif c == 43: # '+'
				# if already read a number-char is time to end
				if in_between:
					out = True
				else:
					in_between = True
					sign = + 1
			elif c == 45: # '-'
				# if already read a number-char is time to end
				if in_between:
					out = True
				else:
					in_between = True
					sign = - 1
			else:
				# check if ASCII is for a NON: valid digits, operator o whitespace
				if c < 48 or c > 57:
					out = True
				else:
					# read a valid ASCII for digits [0--9]
					if not in_between:
						in_between = True
					
					number = number*(10) + (c - 48)

			index += 1

		# checking if the number converted is in [-2^31, 2^31 - 1]
		# -2147483648 low
		# +2147483647 high
		number = number * sign

		if number < -2147483648:
			return -2147483648
		elif number > 2147483647:
			return 2147483647
		else:
			return number
 
solution = Solution()
print(solution.myAtoi('42') == 42)
print(solution.myAtoi('   -42') == -42)
print(solution.myAtoi('4193 with words') == 4193)
print(solution.myAtoi('   ') == 0)
print(solution.myAtoi('41.93') == 41)
print(solution.myAtoi('-2147483650') == -2147483648)
print(solution.myAtoi('words and 987') == 0)
print(solution.myAtoi('+-12') == 0)
print(solution.myAtoi('-+12') == 0)
print(solution.myAtoi('00000-42a1234') == 0)


