from .travelplan import TravelPlan
from reservas import BookingSystem
from colaboracao import CollaborativePlanner
from utils import get_user_input




class Itinerary(TravelPlan):
    def __init__(self, user_id):
        super().__init__()
        self._activities = []
        self._booking_system = BookingSystem()
        self._collaborative_planner = CollaborativePlanner()
        self._user_id = user_id


    def add_activity(self, name):

        if not self._trip_data:
            print("\nPreencha os detalhes da viagem primeiro:")
            horario = get_user_input("Horário de partida: ")
            data = get_user_input("Data da viagem (DD-MM-AAAA): ")
            transporte = get_user_input("Tipo de transporte: ")
            pessoas = int(get_user_input("Quantidade de pessoas: "))

            print("Categorias de viagem:")
            print("1. Trabalho")
            print("2. Amigos")
            print("3. Família")
            print("4. Faculdade")
            category_choice = get_user_input("Escolha a categoria da viagem (1-4): ")
            categories = {"1": "Trabalho", "2": "Amigos", "3": "Família", "4": "Faculdade"}
            categoria = categories.get(category_choice, "Categoria inválida")

            self.set_trip_details(horario, data, transporte, pessoas, categoria)

        self._activities.append({"nome": name})
        print("\nAtividade adicionada com sucesso!\n")


    def remove_activity(self, index):
        if 0 <= index < len(self._activities):
            "atividade removida!"
            return self._activities.pop(index)
        return None

    def exibir_info(self):
        super().exibir_info()

        print("\nAtividades planejadas:")
        for i, atividade in enumerate(self._activities, 1):
            print(f"{i}. {atividade['nome']}")
            if self._trip_data:
                print(f"\n Viagem: {self._trip_data['categoria_da_viagem']}")
                print(f" Horário de partida: {self._trip_data['horario']}")
                print(f" Data: {self._trip_data['data_da_viagem']}")
                print(f" Transporte: {self._trip_data['tipo_de_transporte']}")
                print(f" Pessoas: {self._trip_data['quantidade_de_pessoas']}")
            else:
                print("\n Detalhes da viagem não preenchidos.")

    def book_accommodation(self, destination):
        options = self._booking_system.get_available_options(destination)
        print("\nOpções de hospedagem disponíveis:")
        for i, hotel in enumerate(options['hotels'], 1):
            print(f"{i}. {hotel}")
        
        choice = int(get_user_input("\nEscolha um hotel (número): ")) - 1
        if 0 <= choice < len(options['hotels']):
            hotel = options['hotels'][choice]
            check_in = get_user_input("Data de check-in (DD-MM-AAAA): ")
            check_out = get_user_input("Data de check-out (DD-MM-AAAA): ")
            guests = int(get_user_input("Número de hóspedes: "))
            
            confirmation = self._booking_system.book_hotel(
                destination, hotel, check_in, check_out, guests
            )
            print(confirmation)
    
    def share_with_friends(self, friends):
        itinerary_id = f"itinerary_{self._user_id}_{len(self._activities)}"
        self._collaborative_planner.share_itinerary(itinerary_id, self._user_id, friends)
        print(f"Itinerário compartilhado com {', '.join(friends)}")
    
    def add_collaborator_comment(self, comment):
        itinerary_id = f"itinerary_{self._user_id}_{len(self._activities)}"
        self._collaborative_planner.add_collaborator_comment(itinerary_id, self._user_id, comment)
        print("Comentário adicionado ao itinerário compartilhado")
    
    def get_shared_itineraries(self):
        return self._collaborative_planner.get_shared_itineraries(self._user_id)

