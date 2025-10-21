from distances import ChebyshevDistance, EuclideanDistance, ManthattanDistance
from linkages import SingleLinkage, CompletedLinkage, AverageLinkage, CentroidLinkage, WardLinkage
import numpy as np

data = np.array([
    [1, 2],
    [2, 3],
    [3, 4],
    [8, 8],
    [9, 9],
])

cluster1 = [0, 1]
cluster2 = [2, 3]

distance_metric = ManthattanDistance()
distance_matrix = np.zeros((len(data), len(data)))

for i in range(len(data)):
    for j in range(len(data)):
        distance = distance_metric.calculate(data[i], data[j])
        distance_matrix[i, j] = distance
        distance_matrix[j, i] = distance

single = SingleLinkage()
single_dist = single.calculate(cluster1=cluster1, cluster2=cluster2, distance_matrix=distance_matrix)
print(f'Single Linkage: {single_dist}')

completed = CompletedLinkage()
completed_dist = completed.calculate(cluster1=cluster1, cluster2=cluster2, distance_matrix=distance_matrix)
print(f'Completed Linkage: {completed_dist}')

average = AverageLinkage()
average_dist = average.calculate(cluster1=cluster1, cluster2=cluster2, distance_matrix=distance_matrix)
print(f'Average Linkage: {average_dist}')

centroid = CentroidLinkage()
centroid_dist = centroid.calculate(cluster1=cluster1, cluster2=cluster2, data=distance_matrix)
print(f'Centroid Linkage: {centroid_dist}')

ward = WardLinkage()
ward_dist = ward.calculate(cluster1=cluster1, cluster2=cluster2, data=distance_matrix)
print(f'Ward Linkage: {ward_dist}')
