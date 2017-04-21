import simon_1bit_dfa
import matplotlib.pyplot as plt
import numpy as np

sample_size = 100
iterations = []
for j in range(sample_size):
    iterations.append(simon_1bit_dfa.dfa_1bit())
mean = float(sum(iterations)) / float(sample_size)

x = np.array(iterations)
plt.hist(x, bins=30)
plt.title('Iterations for 128-bit Key 1-bit Fault')
plt.xlabel('Mean: %.2f' % round(mean, 2))
plt.savefig('hist_%d_iter_1_bit.jpg' % sample_size)
