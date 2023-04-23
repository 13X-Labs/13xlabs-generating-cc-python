# 13xlabs Generating CreditCard - Python

## Credit Card Generator

This Python script generates a list of 100 credit card numbers based on user input for the prefix, CCV, and expiration date. If the user does not provide a CCV or expiration date, the script generates random values for these fields. The generated credit card numbers are Luhn-compliant and have a total length of 16 digits.

## Requirements

- Python 3.x

## Usage

Run the script in a Python 3 environment:

```bash
python credit_card_generator.py
```

The script will prompt you to enter the following information:
- Desired prefix for the credit card number (maximum 15 digits)
- Desired CCV (3 digits) or leave it blank to generate randomly
- Desired expiration date (in MM/YY format) or leave it blank to generate randomly

The script will generate a list of 100 credit card numbers using the provided prefix, CCV, and expiration date (or randomly generated values if the user left them blank). The generated numbers will be written to a file named credit_cards_generation.txt, with each credit card number, expiration date, and CCV separated by a pipe (|) character.

Example output:

```python
5568839172436580|12/27|123
5568838247193010|11/24|321
...
```


## Disclaimer
This script is for educational purposes only. Generating and using fake credit card numbers is illegal and unethical. Please do not use this script for any illegal activities. The author is not responsible for any consequences resulting from the misuse of this script.

## License
MIT License

Copyright (c) 2023 Velik Ho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.