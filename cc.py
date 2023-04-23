import random
import datetime
import re

def generate_credit_card_number(prefix, ccv=None, expiration_date=None):
    # Ensure the prefix is a string
    prefix = str(prefix)
    
    # Generate the remaining digits randomly
    account_number = str(random.randint(0, 10**(16-len(prefix)) - 1)).zfill(16 - len(prefix))
    card_number = prefix + account_number

    # Calculate the Luhn checksum
    checksum = 0
    for i, digit in enumerate(card_number[:-1]):
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
        card_number = card_number[:-1] + "0"
    else:
        card_number = card_number[:-1] + str(10 - (checksum % 10))

    # If the user doesn't provide a CCV, generate it randomly (3 digits)
    if ccv is None:
        ccv = str(random.randint(0, 999)).zfill(3)

    # If the user doesn't provide an expiration date, generate it randomly (MM/YY format)
    if expiration_date is None:
        now = datetime.datetime.now()
        expiration_year = now.year + random.randint(1, 6)
        expiration_month = random.randint(1, 12)
        if expiration_month < 10:
            expiration_month = "0" + str(expiration_month)
        else:
            expiration_month = str(expiration_month)
        expiration_date = expiration_month + "/" + str(expiration_year)[2:]

    return (card_number, ccv, expiration_date)

# Get user input for the prefix, CCV, and expiration date
prefix_input = input("Enter the desired prefix for the credit card number (max 15 digits): ")

while True:
    ccv_input = input("Enter the desired CCV (3 digits) or leave blank to generate randomly: ")
    if ccv_input.strip() == "" or (len(ccv_input) == 3 and ccv_input.isdigit()):
        break
    else:
        print("Error: Invalid CCV. Please enter a 3-digit number or leave it blank.")

while True:
    expiration_date_input = input("Enter the desired expiration date (MM/YY) or leave blank to generate randomly: ")
    if expiration_date_input.strip() == "" or re.match(r"^(0[1-9]|1[0-2])/\d{2}$", expiration_date_input):
        break
    else:
        print("Error: Invalid expiration date. Please enter in the format MM/YY or leave it blank.")

# Set CCV and expiration date to None if they are not provided
ccv_input = None if ccv_input.strip() == "" else ccv_input
expiration_date_input = None if expiration_date_input.strip() == "" else expiration_date_input

with open("credit_cards_generation.txt", "w") as f:
    for i in range(100):
        # Generate a new credit card number
        card_number, ccv, expiration_date = generate_credit_card_number(prefix_input, ccv_input, expiration_date_input)
        f.write(card_number + "|" + expiration_date + "|" + ccv + "\n")