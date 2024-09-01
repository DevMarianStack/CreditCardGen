# github : DevMarianStack
import random
from datetime import datetime

# Luhn Algorithm for Card Validation
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

# Function to generate random CVV
def generate_cvv():
    return f"{random.randint(100, 999)}"

# Function to generate random expiry date within the next 5 years
def generate_expiry_date():
    current_year = datetime.now().year
    month = f"{random.randint(1, 12):02d}"
    year = f"{random.randint(current_year + 1, current_year + 5) % 100:02d}"
    return f"{month}/{year}"

# Generate a random credit card number
def generate_card():
    result = []
    while len(result) < 5:  # Generate 5 cards
        x = 0
        nvar = 0
        num = []
        num_n = []
        num_s = []
        for i in range(random.randrange(13, 17)):
            num.append(random.randrange(0, 10))
        for num_x in num[:len(num)-1][::-1]:
            if x == 0:
                num_xx = num_x * 2
                if num_xx > 9:
                    num_xx = num_xx % 10 + 1
                num_n.append(num_xx)
                x = 1
            else:
                num_n.append(num_x)
                x = 0
        for n in num: num_s.append(str(n))
        for n in num_n: nvar += n
        if int(str(nvar * 9)[-1]) == num[-1]:
            card_number = "".join(num_s)
            cvv = generate_cvv()
            expiry_date = generate_expiry_date()
            print(f"Card Number: {card_number}")
            print(f"CVV: {cvv}")
            print(f"Expiry Date: {expiry_date}")
            print("-" * 30)
            result.append(card_number)

# Example usage:
generate_card()
