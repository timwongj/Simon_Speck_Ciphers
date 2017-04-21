import simon_multi_bit_dfa
import matplotlib.pyplot as plt
import numpy as np

bits = 20
sample_size = 100
iterations = []
for j in range(sample_size):
    iterations.append(simon_multi_bit_dfa.dfa_multi_bit(bits))
mean = float(sum(iterations)) / float(sample_size)

x = np.array(iterations)
plt.hist(x, bins=30)
plt.title('Iterations for 128-bit Key %d-bit Fault' % bits)
plt.xlabel('Mean: %.2f' % round(mean, 2))
plt.savefig('hist_%d_iter_%d_bits.jpg' % (sample_size, bits))
