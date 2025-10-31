from agglomerative import AgglomerativeClustering
from distances import EuclideanDistance
from linkages import SingleLinkage
from utils import plot_dendogram
import numpy as np

np.random.seed(42)
data = np.random.rand(10, 2)

for i, j in enumerate(data):
    print(f'Point {i}: {j}')

distance = EuclideanDistance()
linkage = SingleLinkage()

agglomerative = AgglomerativeClustering(distance, linkage)
linkage_matrix = agglomerative.fit(data)

plot_dendogram(linkage_matrix)


