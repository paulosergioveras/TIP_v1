from abc import ABC, abstractmethod

class ISubject(ABC):
    """Interface para o subject (observado)"""
    
    @abstractmethod
    def attach(self, observer):
        """Anexa um observador"""
        pass
    
    @abstractmethod
    def detach(self, observer):
        """Desanexa um observador"""
        pass
    
    @abstractmethod
    def notify(self):
        """Notifica todos os observadores"""
        pass


class IObserver(ABC):
    """Interface para observadores"""
    
    @abstractmethod
    def update(self, subject):
        """Atualiza o observador quando o subject muda"""
        pass


class ItinerarySubject(ISubject):
    """Implementação concreta de Subject para itinerários"""
    
    def __init__(self):
        self._observers = []
        self._state = {}  # Estado do itinerário que será observado
    
    def attach(self, observer):
        """Anexa um observador ao itinerário"""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observador {observer.__class__.__name__} anexado.")
    
    def detach(self, observer):
        """Remove um observador do itinerário"""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observador {observer.__class__.__name__} removido.")
    
    def notify(self):
        """Notifica todos os observadores sobre mudanças"""
        for observer in self._observers:
            observer.update(self)
    
    def set_state(self, key, value):
        """Altera o estado do itinerário e notifica observadores"""
        self._state[key] = value
        self.notify()
    
    def get_state(self):
        """Retorna o estado atual do itinerário"""
        return self._state.copy()


class ActivityObserver(IObserver):
    """Observador que monitora mudanças nas atividades do itinerário"""
    
    def update(self, subject):
        """Reage a mudanças nas atividades"""
        state = subject.get_state()
        if 'activity_added' in state:
            print(f"\nNOTIFICAÇÃO: Nova atividade '{state['activity_added']}' adicionada ao itinerário.")
            # Poderia enviar notificações, atualizações de calendário, etc.
        
        if 'activity_removed' in state:
            print(f"\nNOTIFICAÇÃO: Atividade '{state['activity_removed']}' removida do itinerário.")


class CollaboratorObserver(IObserver):
    """Observador que notifica colaboradores sobre mudanças no itinerário"""
    
    def __init__(self, collaborators=None):
        self._collaborators = collaborators or []
    
    def add_collaborator(self, email):
        """Adiciona um colaborador à lista de notificação"""
        if email not in self._collaborators:
            self._collaborators.append(email)
    
    def update(self, subject):
        """Envia notificações aos colaboradores"""
        state = subject.get_state()
        
        if self._collaborators and ('activity_added' in state or 'activity_removed' in state):
            print("\nNOTIFICAÇÃO: Enviando emails para colaboradores sobre alterações no itinerário:")
            for email in self._collaborators:
                print(f"  - Email enviado para: {email}")


class ExpenseObserver(IObserver):
    """Observador que atualiza despesas quando atividades são adicionadas ou removidas"""
    
    def __init__(self, expense_manager):
        self._expense_manager = expense_manager
    
    def update(self, subject):
        """Atualiza o gerenciador de despesas"""
        state = subject.get_state()
        
        if 'activity_added' in state and 'activity_cost' in state:
            activity = state['activity_added']
            cost = state['activity_cost']
            self._expense_manager.add_expense(f"Atividade: {activity}", cost)
            print(f"\nNOTIFICAÇÃO: Despesa de R$ {cost:.2f} para '{activity}' registrada automaticamente.")
