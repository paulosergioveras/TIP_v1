from itinerary import Itinerary
from factories import get_service_factory
from helpers import get_user_input, show_menu, show_booking_menu, show_preferences_menu




def main():
    user_id = "user_001" 
    factory = get_service_factory()
    
    # Cria os componentes usando a fábrica
    itinerary = Itinerary(user_id)
    destination_info = factory.create_destination_info()
    expense_manager = factory.create_expense_manager()
    preference_manager = factory.create_preference_manager()
    
    while True:
        show_menu()
        choice = get_user_input("Escolha uma opção: ")

        if choice == "1":
            name = get_user_input("Nome da atividade: ")
            itinerary.add_activity(name)
        
        elif choice == "2":
            itinerary.exibir_info()  
            index = int(get_user_input("Digite o número da atividade a ser removida: ")) - 1
            itinerary.remove_activity(index)
        
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
                    destination_info.set_user_preferences(user_id, {"price": price})
                    print("Preferência de preço definida!")
                
                elif pref_choice == "2":
                    continent = get_user_input("Continente preferido (Europa, Ásia, América do Sul, América do Norte, África, Oceania): ")
                    destination_info.set_user_preferences(user_id, {"continent": continent})
                    print("Preferência de continente definida!")
                
                elif pref_choice == "3":
                    activity = get_user_input("Tipo de atividade preferida (Aventura, Cultural, Relaxamento, Gastronomia): ")
                    destination_info.set_user_preferences(user_id, {"activity_type": activity})
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
