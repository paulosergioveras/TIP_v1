# Travel_Itinerary_Planner
 
## ✅ Implemented Features

    - Itinerary Creation and Customization: Users can create and personalize their travel itineraries.

    - Destination Information and Recommendations: Provides relevant information and recommendations for various travel destinations.

    - Booking Integration: ntegrates with booking systems for hotels, flights, and activities.

    - Collaborative Planning Tools: Enables multiple users to collaboratively plan a trip.

    - Travel Guides and Resources: Offers access to travel guides and useful resources.

    - Personalization Based on Preferences: Suggests destinations and activities based on user preferences.

    - Expense Tracking and Budget Management: Tracks travel-related expenses and helps users manage their budgets.

    - User Reviews and Community Input: Incorporates user reviews and community suggestions into the planning process.

## ❌ Not Yet Implemented

    - Map Integration and Route Planning: Integration with maps for route planning and navigation.

    - Mobile Access and Offline Functionality: Support for mobile devices and offline access.

    Why? These features were not implemented due to their complexity.


## 🧠 Design Pattern Used: Factory Method (Creational Pattern)

    Problem Identified
    The system initially created instances of classes like BookingSystem, CollaborativePlanner, and other components directly. This led to:

        Tight coupling between classes

        Difficulties in maintaining and extending the code

        The need to modify multiple parts of the code to add new features

    Solution with Factory Method
    The Factory Method pattern provides an interface for creating objects in a superclass while allowing subclasses to alter the type of objects that are created.

        Benefits for this project:

        Encapsulates and centralizes object creation logic

        Facilitates the addition of new types of services or features

        Reduces coupling between system components

## 🧠 Design Pattern Used: Decorator (Structural Pattern)

    Problem Identified

        The original system did not provide a flexible mechanism to extend the functionality of individual objects without modifying their base structure. For instance, for each new feature such as time validation or budget tracking, the following issues arose:

        Direct modifications to the Itinerary class were necessary

        Specific subclasses needed to be created for each combination of functionalities

        The class hierarchy became increasingly complex and difficult to manage

    Consequences:

        High code duplication

        Difficulty in combining multiple features

        Strong coupling between components

        Complex maintenance when introducing new functionalities

    Solution with Decorator

        Two specific decorators were implemented to address these concerns:

        TimeConflictValidator: Adds time conflict validation to itineraries

        BudgetTrackingDecorator: Adds budget control and tracking to itineraries

    Benefits:

        Flexibility: Decorators can be combined in any order and applied as needed

        Open/Closed Principle: New functionalities can be added without modifying existing code

        Composition Over Inheritance: Prevents subclass explosion by using composition instead of inheritance

        Per-Object Customization: Each instance can have its own set of decorators

## 🧠 Design Pattern Used: Observer (Behavioral Pattern)

    Problem Identified

        In the initial system, interactions between components were tightly coupled, making it difficult to establish communication between independent modules. For example:

        When an activity was added to the itinerary, components such as the expense manager or collaborators were not automatically notified

        Updates in one component required manual changes in other components

        Establishing a consistent flow of updates between related objects was challenging

        Classes that needed to exchange information became strongly coupled

    Solution with Observer

        An observer architecture was implemented with the following components:

        ItinerarySubject: Interface for observable objects

        ObservableItinerary: Concrete class that notifies observers about changes

    Three types of observers:

        ActivityObserver: Monitors activity changes

        CollaboratorObserver: Notifies collaborators about updates

        ExpenseObserver: Automatically updates expense information

    Benefits:

        Low Coupling: Observers do not need to know the specifics of the observed subject

        Automatic Communication: Updates in one component are automatically propagated

        Extensibility: New observers can be easily added

        Component Reusability: Observers can be reused in different contexts

