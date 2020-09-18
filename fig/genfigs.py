import matplotlib.pyplot as plt
import numpy as np

# g(w)
fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.set_title(r'$a=0$', fontsize=20)
ax1.set_xticks([3])
ax1.set_xticklabels([r'$\bar{\omega}$'], fontsize=20)
ax1.set_yticks([1])
ax1.set_yticklabels([r'$g(\omega)$'], fontsize=20)
ax1.tick_params(axis='y', length=0)

ax2.set_title(r'$a\gg0$', fontsize=20)
ax2.set_xticks([3])
ax2.set_xticklabels([r'$\bar{\omega}$'], fontsize=20)
ax2.set_yticks([])
x = np.linspace(0, 6, 200)
y = np.exp(-(x-3)**2)
a = np.exp(-(x-1.5)**2)
b = np.exp(-(x-4.5)**2)
ax1.plot(x, y, 'k')
ax1.axvline(3, dashes=[0, 2, 7, 9], color='k', lw=1)
ax2.plot(x, y**15+a**2*0.3+b**2*0.3, 'k')
ax2.axvline(3, dashes=[0, 2, 7, 9], color='k', lw=1)
#fig.savefig('natural_frequencies.pdf')
plt.show()
