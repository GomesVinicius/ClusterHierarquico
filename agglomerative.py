from hierarchical import HierachicalClustering
import numpy as np

class AgglomerativeClustering(HierachicalClustering):
    def fit(self, data):
        clusters = [
            {
                'id': i,
                'points': [i]
            } for i in range(len(data))
        ]

        distance_matrix = np.zeros( len(data), len(data) )
        next_cluster_index = len(data)
        
        for i in range(len(data)):
            for j in range(len(data)):
                distance = self.distance_strategy.calculate(data[i], data[j])
                distance_matrix[i, j] = distance
                distance_matrix[j, i] = distance

        return clusters
