import random


def xor_division(message, polynomial):
    polynomial_length = len(polynomial)
    current_dividend = int(message[:polynomial_length], 2)

    for bit in message[polynomial_length:]:
        if current_dividend & (1 << (polynomial_length - 1)):
            current_dividend ^= int(polynomial, 2)
        current_dividend <<= 1
        current_dividend |= int(bit)

    if current_dividend & (1 << (polynomial_length - 1)):
        current_dividend ^= int(polynomial, 2)

    remainder = current_dividend & ((1 << polynomial_length) - 1)
    return remainder


if __name__ == "__main__":
    message = "110101101"
    start_message_len = len(message)
    polynomial = "10011"
    zero_cnt = 0
    print("Message:", message)

    if len(message) < 15:
        while len(message) < 15:
            message += '0'
            zero_cnt += 1
    elif len(message) > 15:
        print("You can encode lines only 2-15 length")

    encode_message_len = len(message)

    remainder = xor_division(message, polynomial)
    print("Remainder:", bin(remainder))

    encode_message = int(message, 2)
    encode_message |= remainder

    random_bit_index = random.randint(start_message_len, encode_message_len)
    print("Error index:", random_bit_index)
    encode_message ^= (1 << random_bit_index)

    print("Encode with one bit error:", bin(encode_message))

    encode_message = bin(encode_message)

    syndrome = xor_division(encode_message, polynomial)
    print("Syndrome:", bin(remainder))

    message = int(message, 2)
    message <<= syndrome
    print("Decode message:", bin(message)[0: start_message_len])
