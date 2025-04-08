class PreferenceManager:
    def __init__(self):
        self._preferences = {
            "price": ["Baixo", "Médio", "Alto"],
            "continent": ["Europa", "América do Norte", "Ásia", "América do Sul", "África", "Oceania"],
            "activity_type": ["Aventura", "Cultural", "Relaxamento", "Gastronomia"]
        }
    
    def get_preference_options(self, preference_type):
        return self._preferences.get(preference_type, [])
    
    def set_user_preferences(self, user_id, preferences):
        """Armazena as preferências do usuário"""
        self._preferences[user_id] = preferences
    
    def get_user_preferences(self, user_id):
        """Retorna as preferências do usuário"""
        return self._preferences.get(user_id, {})
