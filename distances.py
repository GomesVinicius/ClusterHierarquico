from abc import ABC, abstractmethod
import numpy as np

class Distance(ABC):
    @abstractmethod

    def calculate(self, point1, point2):
        pass

class EuclideanDistance(Distance):
    def calculate(self, point1, point2):
        # d² = sqrt( a² - b² )
        # return np.sqrt( (point1 - point2) ** 2 )
        return np.linalg.norm(point1 - point2)

class ManthattanDistance(Distance):
    def calculate(self, point1, point2):
        return np.sum(np.abs(point1 - point2))

class ChebyshevDistance(Distance):
    def calculate(self, point1, point2):
        return np.max(np.abs(point1 - point2))
