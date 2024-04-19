from abc import ABC,abstractmethod

class CasinoBuilder(ABC):

    @abstractmethod
    def constructGameTableA(number):
        pass

    @abstractmethod
    def constructGameTableB(number):
        pass

    @abstractmethod
    def constructGameTableC(number):
        pass

    @abstractmethod
    def constructGameTableD(number):
        pass

    @abstractmethod
    def constructBar():
        pass

    @abstractmethod
    def constructTokenCounter():
        pass