from Python.simon import SimonCipher
from Python.simon_multi_bit_dfa import SimonCipherMultiBitDfa


def dfa_multi_bit(bits):

    key = 0xABBAABBAABBAABBAABBAABBAABBAABBA
    plaintext = 0xCCCCAAAA55553333

    my_simon = SimonCipher(key)
    my_simon_1byte_dfa = SimonCipherMultiBitDfa(key)

    num_bits = 64
    leaked_x_t_2 = 0
    solved_bits = [0 for j in range(0, num_bits)]
    iterations = 0

    while sum(solved_bits) != num_bits:
        iterations += 1

        # Encrypt with and without fault
        simon_ciphertext = my_simon.encrypt(plaintext)
        simon_ciphertext_1byte_dfa = my_simon_1byte_dfa.encrypt(plaintext, bits)

        # Extract x and y
        x = simon_ciphertext / (2 ** num_bits)
        y = simon_ciphertext % (2 ** num_bits)
        x_1byte_dfa = simon_ciphertext_1byte_dfa / (2 ** num_bits)
        y_1byte_dfa = simon_ciphertext_1byte_dfa % (2 ** num_bits)

        # Determine fault positions
        e = x ^ x_1byte_dfa ^ my_simon_1byte_dfa.f(y) ^ my_simon_1byte_dfa.f(y_1byte_dfa)
        fault_positions = []
        pos = 0
        while e > 0:
            if e % 2 == 1:
                fault_positions.append(pos)
            e /= 2
            pos += 1

        # Determine usable fault bits
        usable_fault_positions = [0 for j in range(0, num_bits)]
        for pos in fault_positions:
            usable_fault_positions[(pos + 1) % num_bits] += 1
            usable_fault_positions[(pos + 2) % num_bits] += 1
            usable_fault_positions[(pos + 8) % num_bits] += 1

        computed_x_t_2 = y ^ y_1byte_dfa

        # Extract values
        for fault_pos in fault_positions:
            if usable_fault_positions[(fault_pos + 1) % num_bits] == 1:
                leaked_x_t_2 |= (computed_x_t_2 >> (fault_pos + 1) % num_bits) % 2 << ((fault_pos - 7) % num_bits)
                solved_bits[(fault_pos - 7) % num_bits] = 1
            if usable_fault_positions[(fault_pos + 8) % num_bits] == 1:
                leaked_x_t_2 |= (computed_x_t_2 >> (fault_pos + 8) % num_bits) % 2 << ((fault_pos + 7) % num_bits)
                solved_bits[(fault_pos + 7) % num_bits] = 1

    return iterations