import ryser as ry
import vizing as vz

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def draw_pls(F, size):
  cmap_base = plt.get_cmap('tab10', 10)
  new_colors = np.vstack([np.array([0.90, 0.90, 0.90, 1.0]), cmap_base(np.arange(cmap_base.N))])
  custom_cmap = matplotlib.colors.ListedColormap(new_colors)
  matrix = np.zeros((size, size), dtype = int)
  for (i, j), value in F_.items():
    matrix[i, j] = value
  norm = matplotlib.colors.BoundaryNorm(
    np.arange(np.min(matrix) - 0.5, np.max(matrix) + 1.5), len(new_colors) + 1
  )
  mat = plt.matshow(matrix, cmap = custom_cmap, norm = norm)
  plt.axis('off')

F_ = {(0, 0): 1, (0, 1): 10, (1, 5): 1, (2, 6): 3}

draw_pls(F_, 10)

plt.savefig("png/pls-10-before.png", format = "PNG")

