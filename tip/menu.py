from itinerary import Itinerary
from factories import get_service_factory
from helpers import get_user_input, show_menu, show_booking_menu, show_preferences_menu
from decorator import TimeConflictValidator, BudgetTrackingDecorator
from observer import ActivityObserver, CollaboratorObserver, ExpenseObserver
from itinerary import ObservableItinerary

def main():
    user_id = "user_001" 
    factory = get_service_factory()
    destination_info = factory.create_destination_info()
    expense_manager = factory.create_expense_manager()
    preference_manager = factory.create_preference_manager()
    base_itinerary = Itinerary(user_id)
    
    print("\nDeseja habilitar recursos avançados?")
    print("1 - Validação de conflitos de horário")
    print("2 - Rastreamento de orçamento")
    print("3 - Ambos")
    print("4 - Nenhum (itinerário básico)")
    advanced_choice = get_user_input("Escolha uma opção: ")
    
    # Aplica os decoradores conforme a escolha
    if advanced_choice == "1":
        itinerary = TimeConflictValidator(base_itinerary)
        print("Validação de conflitos de horário ativada!")
    elif advanced_choice == "2":
        budget = float(get_user_input("Digite seu orçamento total para a viagem (R$): "))
        itinerary = BudgetTrackingDecorator(base_itinerary, budget)
        print(f"Rastreamento de orçamento ativado! Orçamento total: R$ {budget:.2f}")
    elif advanced_choice == "3":
        budget = float(get_user_input("Digite seu orçamento total para a viagem (R$): "))
        itinerary = TimeConflictValidator(BudgetTrackingDecorator(base_itinerary, budget))
        print("Validação de conflitos e rastreamento de orçamento ativados!")
    else:
        itinerary = base_itinerary
        print("Usando itinerário básico.")
    
    # Criação do itinerário observável para demonstrar o padrão Observer
    observable_itinerary = ObservableItinerary(user_id)
    
    # Adiciona observadores
    activity_observer = ActivityObserver()
    observable_itinerary.attach(activity_observer)
    
    # Adiciona observador de despesas
    expense_observer = ExpenseObserver(expense_manager)
    observable_itinerary.attach(expense_observer)
    
    while True:
        show_menu()
        choice = get_user_input("Escolha uma opção: ")

        if choice == "1":
            name = get_user_input("Nome da atividade: ")
            
            # Se estiver usando o decorador de validação de horário ou orçamento
            if advanced_choice in ["1", "3"]:
                start_time = get_user_input("Horário de início (HH:MM): ")
                end_time = get_user_input("Horário de término (HH:MM): ")
                itinerary.add_activity(name, start_time, end_time)
            elif advanced_choice == "2":
                cost = float(get_user_input("Custo estimado da atividade (R$): "))
                itinerary.add_activity(name, cost)
            else:
                itinerary.add_activity(name)
            
            observable_itinerary.add_activity(name)
        
        elif choice == "2":
            itinerary.exibir_info()  
            index = int(get_user_input("Digite o número da atividade a ser removida: ")) - 1
            removed = itinerary.remove_activity(index)
            
            # Notifica os observadores sobre a remoção
            if removed:
                observable_itinerary.remove_activity(index)
        
        elif choice == "3":
            itinerary.exibir_info()
        
        elif choice == "4":
            price_pref = get_user_input("\nPreferência de preço (Baixo, Médio, Alto ou deixe em branco): ")
            continent_pref = get_user_input("Continente preferido (Europa, Ásia, América do Sul, América do Norte, África, Oceania ou deixe em branco): ")
            destination_info.get_info(price_pref if price_pref else None, 
                                    continent_pref if continent_pref else None)
        
        elif choice == "5":
            categoria = get_user_input("Categoria da despesa: ")
            valor = float(get_user_input("Valor gasto (R$): "))
            expense_manager.add_expense(categoria, valor)
            
            # Pergunta se deseja vincular a despesa a uma atividade
            vincular = get_user_input("Vincular esta despesa a uma atividade? (s/n): ").lower()
            if vincular == 's':
                itinerary.exibir_info()
                if hasattr(itinerary, '_activities') and itinerary._activities:
                    activity_index = int(get_user_input("Número da atividade: ")) - 1
                    if 0 <= activity_index < len(itinerary._activities):
                        activity_name = itinerary._activities[activity_index]['nome']
                        # Notifica os observadores sobre a nova despesa associada à atividade
                        observable_itinerary.set_state('expense_added', valor)
                        observable_itinerary.set_state('expense_activity', activity_name)
                else:
                    print("Não há atividades para vincular.")
        
        elif choice == "6":
            expense_manager.show_expenses()
        
        elif choice == "7":
            destination = get_user_input("Destino para reserva: ")
            while True:
                show_booking_menu()
                booking_choice = get_user_input("Escolha uma opção: ")
                
                if booking_choice == "1":
                    itinerary.book_accommodation(destination)
                elif booking_choice == "2":
                    options = itinerary._booking_system.get_available_options(destination)
                    print("\nVoos disponíveis:")
                    for i, flight in enumerate(options['flights'], 1):
                        print(f"{i}. {flight}")
                    
                    flight_choice = int(get_user_input("\nEscolha um voo (número): ")) - 1
                    if 0 <= flight_choice < len(options['flights']):
                        flight = options['flights'][flight_choice]
                        date = get_user_input("Data do voo (DD-MM-AAAA): ")
                        passengers = int(get_user_input("Número de passageiros: "))
                        
                        confirmation = itinerary._booking_system.book_flight(
                            destination, flight, date, passengers
                        )
                        print(confirmation)
                elif booking_choice == "3":
                    break
                else:
                    print("Opção inválida.")
        
        elif choice == "8":
            friends = get_user_input("Digite os emails dos amigos para compartilhar (separados por vírgula): ").split(',')
            friends = [email.strip() for email in friends]
            itinerary.share_with_friends(friends)
            
            # Demonstração do padrão Observer para notificações
            collaborator_observer = CollaboratorObserver(friends)
            observable_itinerary.attach(collaborator_observer)
            print("Observador de colaboradores adicionado. Colaboradores serão notificados sobre mudanças.")
        
        elif choice == "9":
            destination = get_user_input("Destino para avaliar: ")
            rating = int(get_user_input("Avaliação (1-5 estrelas): "))
            comment = get_user_input("Comentário: ")
            destination_info.add_review(destination, user_id, rating, comment)
            print("Avaliação adicionada com sucesso!")
        
        elif choice == "10":
            while True:
                show_preferences_menu()
                pref_choice = get_user_input("Escolha uma opção: ")
                
                if pref_choice == "1":
                    price = get_user_input("Preferência de preço (Baixo, Médio, Alto): ")
                    preference_manager.set_user_preferences(user_id, {"price": price})
                    destination_info.set_user_preferences(user_id, {"price": price})
                    print("Preferência de preço definida!")
                
                elif pref_choice == "2":
                    continent = get_user_input("Continente preferido (Europa, Ásia, América do Sul, América do Norte, África, Oceania): ")
                    preference_manager.set_user_preferences(user_id, {"continent": continent})
                    destination_info.set_user_preferences(user_id, {"continent": continent})
                    print("Preferência de continente definida!")
                
                elif pref_choice == "3":
                    activity = get_user_input("Tipo de atividade preferida (Aventura, Cultural, Relaxamento, Gastronomia): ")
                    preference_manager.set_user_preferences(user_id, {"activity_type": activity})
                    print("Preferência de atividade definida!")
                
                elif pref_choice == "4":
                    break
                else:
                    print("Opção inválida.")
        
        elif choice == "11":
            print("\nDestinos recomendados para você:")
            recommended = destination_info.get_personalized_recommendations(user_id)
            for dest in recommended:
                print(f"- {dest}")
            if not recommended:
                print("Nenhuma recomendação disponível. Defina suas preferências primeiro.")
        
        elif choice == "12":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida.")

        continue_choice = get_user_input("\nDeseja continuar? (s/n): ").strip().lower()
        if continue_choice != 's':
            print("\nObrigado por usar o planejador de viagens!")
            break

if __name__ == "__main__":
    main()
