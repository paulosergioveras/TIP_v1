class DestinationInfo:
    def __init__(self):
      self._destinations = {
          "Paris": {"descrição": "Cidade Luz, famosa pela Torre Eiffel e pela gastronomia requintada.", "preço": "Alto", "continente": "Europa"},
          "Nova York": {"descrição": "Metrópole vibrante, lar da Estátua da Liberdade e da Times Square.", "preço": "Alto", "continente": "América do Norte"},
          "Tóquio": {"descrição": "Capital do Japão, mescla tecnologia de ponta e tradição, com templos históricos.", "preço": "Alto", "continente": "Ásia"},
          "Roma": {"descrição": "Cidade antiga com o icônico Coliseu e rica história do Império Romano.", "preço": "Médio", "continente": "Europa"},
          "Rio de Janeiro": {"descrição": "Cidade brasileira famosa pela praia de Copacabana e o Cristo Redentor.", "preço": "Médio", "continente": "América do Sul"},
          "Londres": {"descrição": "Cidade multicultural com o Big Ben e a Torre de Londres.", "preço": "Alto", "continente": "Europa"},
          "Cairo": {"descrição": "Cidade egípcia com as Grandes Pirâmides e o Museu Egípcio.", "preço": "Baixo", "continente": "África"},
          "Sydney": {"descrição": "Cidade portuária com a icônica Ópera de Sydney e belas praias.", "preço": "Alto", "continente": "Oceania"},
          "Barcelona": {"descrição": "Cidade espanhola com arquitetura de Gaudí e vida noturna vibrante.", "preço": "Médio", "continente": "Europa"},
          "Pequim": {"descrição": "Capital chinesa com a Cidade Proibida e a Grande Muralha.", "preço": "Médio", "continente": "Ásia"},
          "Cape Town": {"descrição": "Cidade sul-africana com Table Mountain e paisagens deslumbrantes.", "preço": "Baixo", "continente": "África"},
          "Amsterdã": {"descrição": "Cidade dos canais, famosa por seus museus e vida noturna.", "preço": "Médio", "continente": "Europa"},
          "Dubai": {"descrição": "Cidade dos Emirados, conhecida por sua arquitetura moderna e luxo.", "preço": "Alto", "continente": "Ásia"},
          "Lisboa": {"descrição": "Cidade costeira com bondes históricos e o Castelo de São Jorge.", "preço": "Baixo", "continente": "Europa"},
          "Bangkok": {"descrição": "Cidade tailandesa com templos budistas e vida noturna animada.", "preço": "Baixo", "continente": "Ásia"},
          "Machu Picchu": {"descrição": "Cidade Inca antiga nas montanhas peruanas.", "preço": "Baixo", "continente": "América do Sul"},
          "Los Angeles": {"descrição": "Cidade do entretenimento, lar de Hollywood e praias famosas.", "preço": "Alto", "continente": "América do Norte"},
          "Istambul": {"descrição": "Cidade turca que une Europa e Ásia, com a Mesquita Azul.", "preço": "Médio", "continente": "Europa/Ásia"},
          "Reykjavik": {"descrição": "Capital da Islândia, com fontes termais e a Aurora Boreal.", "preço": "Médio", "continente": "Europa"},
          "Mumbai": {"descrição": "Cidade indiana vibrante com Bollywood e Gateway of India.", "preço": "Baixo", "continente": "Ásia"},
          "Buenos Aires": {"descrição": "Cidade argentina com rica cultura do tango e arquitetura colonial.", "preço": "Baixo", "continente": "América do Sul"}
      }
      self._user_preferences = {}
      self._reviews = {}

    def get_info(self, price_preference=None, preferred_continent=None):
      print("\nDestinos disponíveis: ---------------------------------\n")
      if price_preference and preferred_continent:
          filtered_destinations = self._filter_destinations(price_preference, preferred_continent)
          for dest in filtered_destinations:
              print(f'- {dest}')
      else:
          for dest in self._destinations.keys():
              print(f'- {dest}')

      choice = input("\nEscolha um destino para mais informações (digite 'sair' para voltar): ")
      if choice.lower() == 'sair':
          return

      closest_match = self._find_closest_match(choice)
      print(f'\n{self._destinations.get(closest_match, "Destino não encontrado")}')

    def _filter_destinations(self, price_preference, preferred_continent):
      filtered_destinations = []
      for dest, info in self._destinations.items():
          if info["preço"] == price_preference and info["continente"] == preferred_continent:
              filtered_destinations.append(dest)
      return filtered_destinations

    def _find_closest_match(self, user_input):
      user_input_lower = user_input.lower()
      closest_match = None
      min_distance = float('inf')
      for dest in self._destinations.keys():
          dest_lower = dest.lower()
          distance = sum(1 for a, b in zip(user_input_lower, dest_lower) if a != b)
          if distance < min_distance:
              min_distance = distance
              closest_match = dest
      return closest_match
  
    def set_user_preferences(self, user_id, preferences):
        """Define preferências do usuário para personalização"""
        self._user_preferences[user_id] = preferences
    
    def get_personalized_recommendations(self, user_id):
        """Retorna recomendações baseadas nas preferências do usuário"""
        if user_id not in self._user_preferences:
            return self.get_info()
        
        preferences = self._user_preferences[user_id]
        recommended = []
        
        for dest, info in self._destinations.items():
            if (not preferences.get('price') or info['preço'] == preferences['price']) and \
               (not preferences.get('continent') or info['continente'] == preferences['continent']):
                recommended.append(dest)
        
        return recommended
    
    def add_review(self, destination, user, rating, comment):
        """Adiciona uma avaliação de usuário para um destino"""
        if destination not in self._reviews:
            self._reviews[destination] = []
        self._reviews[destination].append({
            "user": user,
            "rating": rating,
            "comment": comment
        })
    
    def get_reviews(self, destination):
        """Retorna todas as avaliações para um destino"""
        return self._reviews.get(destination, [])
    
    def get_average_rating(self, destination):
        """Calcula a avaliação média de um destino"""
        reviews = self._reviews.get(destination, [])
        if not reviews:
            return 0
        return sum(review['rating'] for review in reviews) / len(reviews)
