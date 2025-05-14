from abc import ABC, abstractmethod
from itinerary import Itinerary

class ItineraryDecorator(ABC):
    """Classe base para todos os decoradores de itinerário"""
    
    def __init__(self, itinerary):
        self._itinerary = itinerary
    
    @abstractmethod
    def add_activity(self, name):
        pass
    
    @abstractmethod
    def remove_activity(self, index):
        pass
    
    @abstractmethod
    def exibir_info(self):
        pass
    
    # Método para acessar outros métodos do itinerário
    def __getattr__(self, name):
        return getattr(self._itinerary, name)


class TimeConflictValidator(ItineraryDecorator):
    """Decorador que valida conflitos de horário ao adicionar atividades"""
    
    def __init__(self, itinerary):
        super().__init__(itinerary)
        self._activity_times = {}  # Armazena os horários das atividades
    
    def add_activity(self, name, start_time=None, end_time=None):
        """Adiciona uma atividade após validar conflitos de horário"""
        if start_time and end_time:
            # Verifica conflitos
            for activity, times in self._activity_times.items():
                if self._has_conflict(start_time, end_time, times["start"], times["end"]):
                    print(f"\nALERTA: Conflito de horário detectado com a atividade '{activity}'!")
                    choice = input("Deseja adicionar mesmo assim? (s/n): ").lower()
                    if choice != 's':
                        print("Atividade não adicionada devido ao conflito.")
                        return False
            
            # Armazena os horários da nova atividade
            self._activity_times[name] = {"start": start_time, "end": end_time}
        
        # Chama o método original após a validação
        self._itinerary.add_activity(name)
        return True
    
    def remove_activity(self, index):
        """Remove uma atividade e seus horários armazenados"""
        activity = self._itinerary.remove_activity(index)
        if activity and activity["nome"] in self._activity_times:
            del self._activity_times[activity["nome"]]
        return activity
    
    def exibir_info(self):
        """Exibe as informações do itinerário com horários detalhados"""
        self._itinerary.exibir_info()
        
        if self._activity_times:
            print("\nDetalhes de horários das atividades:")
            for activity, times in self._activity_times.items():
                print(f"- {activity}: {times['start']} até {times['end']}")
    
    def _has_conflict(self, new_start, new_end, existing_start, existing_end):
        """Verifica se há conflito entre dois horários"""
        return (new_start < existing_end and new_end > existing_start)


class BudgetTrackingDecorator(ItineraryDecorator):
    """Decorador que adiciona rastreamento de orçamento às atividades"""
    
    def __init__(self, itinerary, total_budget):
        super().__init__(itinerary)
        self._total_budget = total_budget
        self._activity_costs = {}
        self._remaining_budget = total_budget
    
    def add_activity(self, name, cost=0):
        """Adiciona uma atividade com seu custo associado"""
        if cost > self._remaining_budget:
            print(f"\nALERTA: O custo desta atividade (R$ {cost:.2f}) excede o orçamento restante (R$ {self._remaining_budget:.2f})!")
            choice = input("Deseja adicionar mesmo assim? (s/n): ").lower()
            if choice != 's':
                print("Atividade não adicionada devido a restrições orçamentárias.")
                return False
        
        self._activity_costs[name] = cost
        self._remaining_budget -= cost
        self._itinerary.add_activity(name)
        print(f"Orçamento restante: R$ {self._remaining_budget:.2f}")
        return True
    
    def remove_activity(self, index):
        """Remove uma atividade e ajusta o orçamento"""
        activity = self._itinerary.remove_activity(index)
        if activity and activity["nome"] in self._activity_costs:
            cost = self._activity_costs[activity["nome"]]
            self._remaining_budget += cost
            del self._activity_costs[activity["nome"]]
            print(f"Orçamento restante após remoção: R$ {self._remaining_budget:.2f}")
        return activity
    
    def exibir_info(self):
        """Exibe as informações do itinerário com detalhes de custos"""
        self._itinerary.exibir_info()
        
        print("\nDetalhes de custos das atividades:")
        total_spent = 0
        for activity, cost in self._activity_costs.items():
            print(f"- {activity}: R$ {cost:.2f}")
            total_spent += cost
        
        print(f"\nOrçamento total: R$ {self._total_budget:.2f}")
        print(f"Total gasto: R$ {total_spent:.2f}")
        print(f"Orçamento restante: R$ {self._remaining_budget:.2f}")
