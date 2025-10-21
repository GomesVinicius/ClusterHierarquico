from abc import ABC, abstractmethod
import numpy as np

class LinkageStrategy(ABC):
    @abstractmethod
    def calculate(self, cluster1, cluster2, distance_matrix):
        pass

class SingleLinkage(LinkageStrategy):
    def calculate(self, cluster1, cluster2, distance_matrix):
        return np.min(
            [distance_matrix[i, j] for i in cluster1 for j in cluster2]
        )

class CompletedLinkage(LinkageStrategy):
    def calculate(self, cluster1, cluster2, distance_matrix):
        return np.max(
            [distance_matrix[i, j] for i in cluster1 for j in cluster2]
        )

class AverageLinkage(LinkageStrategy):
    def calculate(self, cluster1, cluster2, distance_matrix):
        return np.mean(
            [distance_matrix[i, j] for i in cluster1 for j in cluster2]
        )

class CentroidLinkage(LinkageStrategy):
    def calculate(self, cluster1, cluster2, data):
        centroid1 = np.mean(data[cluster1], axis=0)
        centroid2 = np.mean(data[cluster2], axis=0)

        return np.linalg.norm(centroid1 - centroid2)

class WardLinkage(LinkageStrategy):
    def calculate(self, cluster1, cluster2, data):
        centroid1 = np.mean(data[cluster1], axis=0)
        centroid2 = np.mean(data[cluster2], axis=0)

        distance_centroids = np.sum((centroid1 - centroid2) ** 2)

        n1 = len(cluster1)
        n2 = len(cluster2)

        ward_distance = (n1 * n2) / (n1 + n2) * distance_centroids

        return ward_distance
