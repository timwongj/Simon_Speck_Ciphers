import simon_1bit_dfa
import matplotlib.pyplot as plt
import numpy as np

sample_size = 10000
iterations = []
for i in range(sample_size):
    iterations.append(simon_1bit_dfa.dfa_1bit())
mean = sum(iterations) / sample_size

x = np.array(iterations)
plt.hist(x, bins=30)
# plt.ylabel('Sample Size: %d, Mean: %f', sample_size, mean)
plt.savefig('histogram.jpg')

print mean
