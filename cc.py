import random
import datetime

def generate_credit_card_number():
    # Generate the first 10 digits randomly
    prefix = "552426"
    account_number = str(random.randint(0, 999999999)).zfill(9)
    card_number = prefix + account_number

    # Calculate the Luhn checksum
    checksum = 0
    for i, digit in enumerate(card_number):
        if i % 2 == 0:
            # Double every other digit, starting from the right
            doubled_digit = int(digit) * 2
            if doubled_digit > 9:
                # If the result is a two-digit number, add the digits together
                doubled_digit = int(str(doubled_digit)[0]) + int(str(doubled_digit)[1])
            checksum += doubled_digit
        else:
            # Add the other digits together
            checksum += int(digit)

    # Add the checksum digit to the end of the card number
    if checksum % 10 == 0:
        card_number += "0"
    else:
        card_number += str(10 - (checksum % 10))

    # Generate the CCV code (3 digits)
    ccv = str(random.randint(0, 999)).zfill(3)

    # Generate the expiration date (MM/YY format)
    now = datetime.datetime.now()
    expiration_year = now.year + random.randint(1, 6)
    expiration_month = random.randint(1, 12)
    if expiration_month < 10:
        expiration_month = "0" + str(expiration_month)
    else:
        expiration_month = str(expiration_month)
    expiration_date = expiration_month + "/" + str(expiration_year)[2:]

    return (card_number, ccv, expiration_date)


with open("credit_cards_generation.txt", "w") as f:
    for i in range(100):
        # Generate a new credit card number
        card_number, ccv, expiration_date = generate_credit_card_number()
        f.write(card_number + "|" + expiration_date + "|" + ccv + "\n")