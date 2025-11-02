from agglomerative import AgglomerativeClustering
from diviseve import PrimDivisionStrategy
from distances import ManthattanDistance, ChebyshevDistance
from linkages import SingleLinkage
import numpy as np

data = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 8],
    [9, 9],
])

index = list(range(len(data)))

distance_strategy = ChebyshevDistance()
prim_strategy = PrimDivisionStrategy()

mst = prim_strategy.compute_mst(data, distance_strategy, index)
print(mst)

for edge in mst.edges(data=True):
    print(f'{edge[0]} - {edge[1]} peso: {edge[2]['weight']}')

subgraphs = prim_strategy.divided(mst)
for i, subgraphs in enumerate(subgraphs, 1):
    print(f'Cluster {i}: {subgraphs}')

# np.random.seed(42)
# data = np.random.rand(10, 2)

# for i, j in enumerate(data):
#     print(f'Point {i}: {j}')

# distance = EuclideanDistance()
# linkage = SingleLinkage()

# agglomerative = AgglomerativeClustering(distance, linkage)
# test = agglomerative.fit(data)
# print(test)
