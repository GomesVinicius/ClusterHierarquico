from diviseve import DivisiveClustering, PrimDivisionStrategy
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

division_strategy = PrimDivisionStrategy()
diviseve = DivisiveClustering(distance, None, division_strategy)
linkage_matrix = diviseve.fit(data)
print(linkage_matrix, 'AAAAAAAAAAAAAAAAAAAA')

plot_dendogram(linkage_matrix)


