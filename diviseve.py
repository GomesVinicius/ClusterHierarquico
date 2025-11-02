from hierarchical import HierachicalClustering
from linkages import LinkageStrategy
from abc import ABC, abstractmethod
from distances import Distance
import networkx as nx
import numpy as np

class DivisionStrategy(ABC):

    @abstractmethod
    def divided(self, param):
        pass

class PrimDivisionStrategy(DivisionStrategy):
    
    def compute_mst(self, data, distance_strategy, index):
        G = nx.Graph()

        for i in index:
            for j in index:
                if j <= i:
                    continue
            
                dist = distance_strategy.calculate(data[i], data[j])
                G.add_edge(i, j, weight=dist)

        
        mst = nx.minimum_spanning_tree(G, algorithm='prim')
        return mst

    def divided(self, param):
        if param.number_of_edges() == 0:
            self.last_removed_edge_weight = 0
            return [list(param.nodes())]
        
        max_edge = max( param.edges(data=True), key=lambda x: x[2]['weight'] )
        
        self.last_removed_edge_weight = max_edge[2]['weight']

        param.remove_edge(max_edge[0], max_edge[1])
        components = list(nx.connected_components(param))

        return [list(component) for component in components]

class DivisiveClustering(HierachicalClustering):
    def __init__(self, distance_strategy: Distance, linkage_strategy: LinkageStrategy, division_strategy) -> None:
        super().__init__(distance_strategy, linkage_strategy)

        self.division_strategy = division_strategy
        self.data = None
        self.linkage_matrix = []
        self.cluster_id_counter = None
        
    def fit(self, data):
        self.data = data
        self.n_samples = data.shape[0]
        self.cluster_id_counter = self.n_samples
        self.initial_cluster = tuple(sorted(range(self.n_samples)))
        self._divide_clusters(data, self.initial_cluster)
        self.linkage_matrix = np.array(self.linkage_matrix)

        return self.linkage_matrix

    def _divide_clusters(self, data, cluster):
        if len(cluster) == 1:
            return cluster[0]
        
        mst = self.division_strategy.compute_mst(data, self.distance_strategy, cluster)
        subclusters = self.division_strategy.divided(mst)

        split_distances = self.division_strategy.last_removed_edge_weight

        left_cluster = tuple(sorted(subclusters[0]))
        right_cluster = tuple(sorted(subclusters[1]))

        left_id = self._divide_clusters(data, left_cluster)
        right_id = self._divide_clusters(data, right_cluster)

        current_cluster_id = self.cluster_id_counter
        self.cluster_id_counter += 1

        sample_count = len(cluster)

        self.linkage_matrix.append([left_id, right_id, split_distances, sample_count])

        return current_cluster_id
