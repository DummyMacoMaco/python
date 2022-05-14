"""
input: a signed 32-bit integer x,

output: x with its digits reversed. 
		If reversing x causes the value to go outside the signed 32-bit integer 
		range [-2^31, 2^31 - 1], then return 0.
		# -2147483648 low
		# +2147483647 high

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
	def reverse(self, x: int):

		INT_MAX = +2147483647
		
		# il segno del numero va mantenuto per il reversedNumber
		if x < 0:
			sign = - 1
		else:
			sign = 1

		# l'operatore modulo fornisce il resto su dividendo > 0
		x *= sign

		reversedNumber = 0
		tmp = 0
		# modulo per ottenere il resto della divisione intera
		# la divisione intera per 10 azzererà il dividendo ad un certo punto
		while x != 0:
			resto = x % 10

			# test se occorre OVERFLOW prima di effettuare aggiornatmento
			# il +1 server per testare anche numero negativo di partenza
			# test effettuato dopo aver convertito il numero in intero positivo
			"""
			reversedNumber <= INT_MAX + 1 (overflow)
			se si testa il risultato che si avrebbe dopo l'aggiornamento allora
			reversedNumber * 10 + resto <= INT_MAX + 1
			reversedNumber * 10 <= INT_MAX - resto + 1
			reversedNumber <= (INT_MAX - resto + 1) // 10 NB si testano interi fra loro
			in questo modo si conduce il test nella ipotesi che numeri superiori ai 32 bit non siano rappresentabili
			nella macchina, infatti (INT_MAX - resto + 1) // 10 è sicuramente nei 32 bit di rappresentazione richiesti
			"""
			try:
				if reversedNumber > (INT_MAX - resto + 1) // 10:
					raise ValueError('overflow')
					
			except ValueError as e:
				print(e)
				return 0
			
			reversedNumber = (reversedNumber * 10) + resto
			# floor division
			x = x // 10

		return reversedNumber * sign



solution = Solution()
print(solution.reverse(123) == 321)
print(solution.reverse(-123) == -321)
print(solution.reverse(120) == 21)
print(solution.reverse(1463847412) == 2147483641)
print(solution.reverse(2147483647) == 0)