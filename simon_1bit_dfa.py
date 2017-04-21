from Python.simon import SimonCipher
from Python.simon_1bit_dfa import SimonCipher1BitDfa
import math


def dfa_1bit():
    key = 0xABBAABBAABBAABBAABBAABBAABBAABBA
    plaintext = 0xCCCCAAAA55553333

    my_simon = SimonCipher(key)
    my_simon_1bit_dfa = SimonCipher1BitDfa(key)

    num_bits = 64
    leaked_x_t_2 = 0
    solved_bits = [0 for j in range(0, num_bits)]
    iterations = 0

    while sum(solved_bits) != num_bits:
        iterations += 1

        # Encrypt with and without fault
        simon_ciphertext = my_simon.encrypt(plaintext)
        simon_ciphertext_1bit_dfa = my_simon_1bit_dfa.encrypt(plaintext)

        # Extract x and y
        x = simon_ciphertext / (2 ** num_bits)
        y = simon_ciphertext % (2 ** num_bits)
        x_1bit_dfa = simon_ciphertext_1bit_dfa / (2 ** num_bits)
        y_1bit_dfa = simon_ciphertext_1bit_dfa % (2 ** num_bits)

        # Determine fault position
        e = x ^ x_1bit_dfa ^ my_simon_1bit_dfa.f(y) ^ my_simon_1bit_dfa.f(y_1bit_dfa)
        fault_pos = int(math.log(e, 2))

        # Extract value
        computed_x_t_2 = y ^ y_1bit_dfa
        leaked_x_t_2 |= (computed_x_t_2 >> (fault_pos + 1) % num_bits) % 2 << ((fault_pos - 7) % num_bits)
        leaked_x_t_2 |= (computed_x_t_2 >> (fault_pos + 8) % num_bits) % 2 << ((fault_pos + 7) % num_bits)

        solved_bits[(fault_pos - 7) % num_bits] = 1
        solved_bits[(fault_pos + 7) % num_bits] = 1

    return iterations
