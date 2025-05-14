from abc import ABC, abstractmethod

class TravelPlan(ABC):
    def __init__(self):
        self._trip_data = {}

    def set_trip_details(self, horario, data, transporte, pessoas, categoria):
        self._trip_data = {
            "horario": horario,
            "data_da_viagem": data,
            "tipo_de_transporte": transporte,
            "quantidade_de_pessoas": pessoas,
            "categoria_da_viagem": categoria
        }

    def get_trip_details(self):
        return self._trip_data.copy()

    @abstractmethod
    def exibir_info(self):

        pass
