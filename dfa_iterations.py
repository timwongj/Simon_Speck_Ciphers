import simon_multi_bit_dfa
import matplotlib.pyplot as plt
import numpy as np

means = []
for bits in range(1, 55):
    print bits
    sample_size = 10
    iterations = []
    for j in range(sample_size):
        iterations.append(simon_multi_bit_dfa.dfa_multi_bit(bits))
    mean = float(sum(iterations)) / float(sample_size)
    means.append(mean)

x = np.array(means)
plt.plot(x)
plt.xlabel('Fault Bits')
plt.ylabel('Iterations')
plt.savefig('means.jpg')
