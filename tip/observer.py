from abc import ABC, abstractmethod

class ISubject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    
    @abstractmethod
    def detach(self, observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass

class IObserver(ABC):
    @abstractmethod
    def update(self, subject):
        pass

class ItinerarySubject(ISubject):
    def __init__(self):
        self._observers = []
        self._state = {}  # Estado do itinerário que será observado
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observador {observer.__class__.__name__} anexado.")
    
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observador {observer.__class__.__name__} removido.")
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, key, value):
        self._state[key] = value
        self.notify()
    
    def get_state(self):
        return self._state.copy()


class ActivityObserver(IObserver):
    def update(self, subject):
        state = subject.get_state()
        if 'activity_added' in state:
            print(f"\nNOTIFICAÇÃO: Nova atividade '{state['activity_added']}' adicionada ao itinerário.")
        
        if 'activity_removed' in state:
            print(f"\nNOTIFICAÇÃO: Atividade '{state['activity_removed']}' removida do itinerário.")


class CollaboratorObserver(IObserver):
    def __init__(self, collaborators=None):
        self._collaborators = collaborators or []
    
    def add_collaborator(self, email):
        if email not in self._collaborators:
            self._collaborators.append(email)
    
    def update(self, subject):
        state = subject.get_state()
        
        if self._collaborators and ('activity_added' in state or 'activity_removed' in state):
            print("\nNOTIFICAÇÃO: Enviando emails para colaboradores sobre alterações no itinerário:")
            for email in self._collaborators:
                print(f"  - Email enviado para: {email}")


class ExpenseObserver(IObserver):
    def __init__(self, expense_manager):
        self._expense_manager = expense_manager
    
    def update(self, subject):
        state = subject.get_state()
        
        if 'activity_added' in state and 'activity_cost' in state:
            activity = state['activity_added']
            cost = state['activity_cost']
            self._expense_manager.add_expense(f"Atividade: {activity}", cost)
            print(f"\nNOTIFICAÇÃO: Despesa de R$ {cost:.2f} para '{activity}' registrada automaticamente.")
