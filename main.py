# author: Marian
# team: DevMarianStack
# sample script for luhn algorithm
import random

g = "\x1b[1;32m" # green color format
n = "\x1b[0m" # normal color format

result = []
f = open("result.txt","w")
while True:
	if len(result) > 10: break
	x = 0
	nvar = 0
	num = []
	num_n = []
	num_s = []
	for i in range(random.randrange(13, 17)):
		num.append(random.randrange(0,10))
	for num_x in num[:len(num)-1][::-1]:
		if x == 0:
			num_xx = num_x * 2
			if num_xx > 9:
				num_xx = num_xx % 10 + 1
			num_n.append(num_xx)
			x = 1
		elif x == 1:
			num_n.append(num_x)
			x = 0
	for n in num: num_s.append(str(n))
	for n in num_n: nvar+=n
	if int(str(nvar * 9)[-1]) == num[-1]:
		print(f"{g}{''.join(num_s)}{n}")
		f.write("".join(num_s)+"\n")
		result.append("".join(num_s))


# Credit Card Validator using Luhn Algorithm
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

def is_valid_card(card_number):
    return luhn_checksum(card_number) == 0

# Example Usage of the Validator
# Replace `card_number` with the generated number to validate
# card_number = "1234567890123456"
# print(is_valid_card(card_number))
