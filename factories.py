from abc import ABC, abstractmethod
from booking import BookingSystem
from collaboration import CollaborativePlanner
from destiny import DestinationInfo
from expenses import ExpenseManager
from preferences import PreferenceManager




class ServiceFactory(ABC):
    """Factory Method abstrato para serviços do sistema de viagens"""
    
    @abstractmethod
    def create_booking_system(self):
        pass
    
    @abstractmethod
    def create_collaborative_planner(self):
        pass
    
    @abstractmethod
    def create_destination_info(self):
        pass
    
    @abstractmethod
    def create_expense_manager(self):
        pass
    
    @abstractmethod
    def create_preference_manager(self):
        pass

class StandardServiceFactory(ServiceFactory):
    """Implementação concreta da fábrica de serviços padrão"""
    
    def create_booking_system(self):
        return BookingSystem()
    
    def create_collaborative_planner(self):
        return CollaborativePlanner()
    
    def create_destination_info(self):
        return DestinationInfo()
    
    def create_expense_manager(self):
        return ExpenseManager()
    
    def create_preference_manager(self):
        return PreferenceManager()

# Função para obter a fábrica de serviços
def get_service_factory():
    return StandardServiceFactory()
