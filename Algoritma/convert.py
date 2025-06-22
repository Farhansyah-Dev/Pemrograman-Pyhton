# The following code converts decimal to binary, octal and hexadecimal

# Defining Functions

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    return binary

def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal = decimal // 8
    return octal

def decimal_to_hexadecimal(decimal):
    hexadecimal = ""
    while decimal > 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
            decimal = decimal // 16
        return hexadecimal

# Taking user input
decimal = int(input("Enter a decimal number to convert: "))
print(f"The binary equivalent of {decimal} is {decimal_to_binary(decimal)}")
print(f"The octal equivalent of {decimal} is {decimal_to_octal(decimal)}")
print(f"The hexadecimal equivalent of {decimal} is {decimal_to_hexadecimal(decimal)}")