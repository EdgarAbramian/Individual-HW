from matplotlib import pyplot as plt
import numpy as np

x = [0.63,
0.66,
1,
1.5,
2,
2.5,
3,
3.55,
4,
5.5]
y = [0.35,
0.3,
0.45,
0.6,
0.7,
0.8,
0.9,
1,
1.05,
1.15,]
plt.plot(x, y)

plt.savefig('fil.png')