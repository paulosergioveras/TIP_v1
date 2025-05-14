class BookingSystem:
    def __init__(self):
        self._available_hotels = {
            "Paris": ["Hotel Paris", "Grand Hotel", "Eiffel View"],
            "Nova York": ["NY Central", "Manhattan Suites", "Brooklyn Inn"],
            "Tóquio": ["Tokyo Towers", "Sakura Hotel", "Shinjuku Plaza"]
        }
        self._available_flights = {
            "Paris": ["AF123", "DL456", "BA789"],
            "Nova York": ["AA101", "UA202", "DL303"],
            "Tóquio": ["JL505", "NH606", "AA707"]
        }
    
    def book_hotel(self, destination, hotel_name, check_in, check_out, guests):
        if destination in self._available_hotels and hotel_name in self._available_hotels[destination]:
            return f"Reserva confirmada no {hotel_name} em {destination} de {check_in} a {check_out} para {guests} hóspedes."
        return "Hotel não disponível para reserva."
    
    def book_flight(self, destination, flight_number, date, passengers):
        if destination in self._available_flights and flight_number in self._available_flights[destination]:
            return f"Voo {flight_number} para {destination} em {date} reservado para {passengers} passageiros."
        return "Voo não disponível."
    
    def get_available_options(self, destination):
        return {
            "hotels": self._available_hotels.get(destination, []),
            "flights": self._available_flights.get(destination, [])
        }
