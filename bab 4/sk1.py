def dectobin(n):
	a = []
	while n >= 1:
		b = n % 2
		n = n / 2
		a.append(b)
	print a[::-1]

def main():
	n = int(raw_input("Input Decimal = "))
	dectobin(n)

if __name__ == '__main__':
	main()
