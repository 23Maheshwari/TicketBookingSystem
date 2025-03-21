# TicketBookingSystem

Overview:
This project is a Ticket Booking System implemented in Python. It allows users to book, cancel, and manage tickets for different types of events such as Movies, Concerts, and Sports. The system is designed using Object-Oriented Programming (OOP) principles and follows best practices for inheritance, polymorphism, abstraction, and interface implementation.

Features:
•	Event Management 
    o	Create different event types (Movies, Concerts, Sports)
    o	Store and retrieve event details
•	Venue Management 
    o	Define venue details for events
•	Customer Management 
    o	Add customer details with name, email, and phone number
•	Ticket Booking System 
    o	Book tickets for an event
    o	Cancel booked tickets
    o	Calculate total booking cost
    o	Retrieve available ticket count
•	Exception Handling 
    o	Handles invalid booking requests and missing event IDs
•	Data Storage 
    o	Uses Python collections (List, Set, Map) for data management
    o	Implements database connectivity to store and retrieve records
    
Technologies Used:
    •	Python
    •	OOP Concepts (Classes, Inheritance, Polymorphism, Abstraction, Interfaces)
    •	Exception Handling
    •	Collections (List, Set, Map)
    •	SQLite/MySQL (Database Integration)
    
Advantages:
    •	User-Friendly: Simple and easy-to-use interface for booking and managing tickets.
    •	Efficient Data Handling: Uses Python collections and database integration for optimized storage.
    •	Error Handling: Robust exception management to prevent crashes and incorrect bookings.
    •	Scalability: Can be extended to support more event types and users.
    •	Automation: Reduces manual efforts in booking and event management.
    •	Future Integration: Can be integrated with web or mobile applications for a better user experience.
    
Usage:
1.	Create an Event 
    o	Enter event details like name, date, time, venue, total seats, and ticket price.
2.	Book Tickets 
    o	Select an event and specify the number of tickets.
3.	Cancel Booking 
    o	Cancel a booking using the booking ID.
4.	Check Available Tickets 
    o	View remaining seats for an event.
5.	View Event Details 
    o	Retrieve event details using event ID.
  	
Exception Handling:
•	EventNotFoundException: Thrown when a user tries to book an event that doesn't exist.
•	InvalidBookingIDException: Raised when an invalid booking ID is entered.
•	NullPointerException Handling: Managed in the main program to avoid unexpected crashes.
