from abc import ABC, abstractmethod
from distances import Distance
from linkages import LinkageStrategy

class HierachicalClustering(ABC):
    def __init__(self, distance_strategy: Distance, linkage_strategy: LinkageStrategy) -> None:
        self.distance_strategy = distance_strategy
        self.linkage_strategy = linkage_strategy

    @abstractmethod
    def fit(self, data):
        pass
