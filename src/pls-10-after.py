import ryser as ry
import vizing as vz

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def draw_ls(F, size):
  matrix = np.zeros((size, size), dtype = int)
  for (i, j), value in F_.items():
    matrix[i, j] = value
  mat = plt.matshow(matrix, cmap = plt.get_cmap('tab10', size))
  plt.axis('off')


F = {1: 1, 2: 10, 15: 1, 26: 3}

G = ry.pls_list_colouring_problem(F, 10)

CP = vz.edge_list_colouring_problem(G, directed = True)
F_ = CP.getSolution()

draw_ls(F_, 10)

plt.savefig("png/pls-10-after.png", format = "PNG")
