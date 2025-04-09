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


## Design Pattern Used: Factory Method (Creational Pattern)

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