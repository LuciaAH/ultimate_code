import random
code = random.randint(1,100)
a = 1
c = 100
while True:
	print ('[', a, '~', c, ']')
	guess = int (input ('請猜一數字：'))
	if guess != code:
		if guess > code:
			c = guess
		else:
			a = guess
		print ('猜錯囉!')
	else:
		print ('終於猜對了!')
		break
