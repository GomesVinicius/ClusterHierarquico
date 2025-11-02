from abc import ABC, abstractmethod
from distances import Distance
from linkages import LinkageStrategy
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
            return [list(param.nodes())]
        
        max_edge = max( param.edges(data=True), key=lambda x: x[2]['weight'] )
        param.remove_edge(max_edge[0], max_edge[1])

        components = list(nx.connected_components(param))

        return [list(component) for component in components]
