from abc import ABC,abstractmethod


class Route(ABC):
    
    @abstractmethod
    def destroy(self):
        pass
    