import ryser as ry
import vizing as vz

import numpy as np
import matplotlib.pyplot as plt

F = {1:1, 2:2, 6:1}
G = ry.pls_list_colouring_problem(F, 3)

CP = vz.edge_list_colouring_problem(G, directed = True)

matrix = np.zeros((3, 3), dtype = int)

for (i, j), value in CP.getSolution().items():
        matrix[i, j] = value

plt.imshow(matrix, cmap = 'tab10')
plt.axis('off')

plt.savefig("png/pls-3.png", format = "PNG")
