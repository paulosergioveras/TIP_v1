from itinerario.travelplan import TravelPlan

class ExpenseManager(TravelPlan):
    def __init__(self):
        super().__init__()
        self._expenses = []

    def add_expense(self, categoria, valor):
        self._expenses.append({"categoria": categoria, "valor": valor})

    def show_expenses(self):
        print("\nDespesas registradas:")
        for exp in self._expenses:
            print(f'- {exp["categoria"]}: R$ {exp["valor"]:.2f}')

    def exibir_info(self):
        super().exibir_info()
        print("\nDespesas da viagem:")
        self.show_expenses()
