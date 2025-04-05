class Event:
    def __init__(self, event_name=None, event_date=None, event_time=None, venue_name=None,
                 total_seats=0, available_seats=0, ticket_price=0.0, event_type=None):
        self.event_name = event_name
        self.event_date = event_date
        self.event_time = event_time
        self.venue_name = venue_name
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type

    def calculate_total_revenue(self):
        booked_tickets = self.total_seats - self.available_seats
        return booked_tickets * self.ticket_price

    def getBookedNoOfTickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked successfully!")
        else:
            print("Not enough seats available!")

    def cancel_booking(self, num_tickets):
        if num_tickets <= (self.total_seats - self.available_seats):
            self.available_seats += num_tickets
            print(f"{num_tickets} tickets canceled successfully!")
        else:
            print("Cannot cancel more tickets than booked!")

    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Date: {self.event_date}")
        print(f"Time: {self.event_time}")
        print(f"Venue: {self.venue_name}")
        print(f"Total Seats: {self.total_seats}")
        print(f"Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}")
        print(f"Event Type: {self.event_type}")


class Venue:
    def __init__(self, venue_id=None, address=None):
        self.venue_id = venue_id
        self.address = address

    def display_venue_details(self):
        print(f"Venue ID: {self.venue_id}")
        print(f"Address: {self.address}")


class Customer:
    def __init__(self, customer_id=None, customer_name=None, email=None, phone_number=None, booking_id=None):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.email = email
        self.phone_number = phone_number
        self.booking_id = booking_id

    def get_customer_name(self):
        return self.customer_name

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_booking_id(self):
        return self.booking_id

    def set_customer_name(self, customer_name):
        self.customer_name = customer_name

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_booking_id(self, booking_id):
        self.booking_id = booking_id

    def display_customer_details(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Booking ID: {self.booking_id}")


class Booking:
    def __init__(self, booking_id, event: Event, customer: Customer, num_tickets):
        self.booking_id = booking_id
        self.event = event
        self.customer = customer
        self.num_tickets = num_tickets
        self.total_cost = 0

    def calculate_booking_cost(self):
        self.total_cost = self.event.ticket_price * self.num_tickets
        return self.total_cost

    def book_tickets(self):
        if self.event.available_seats >= self.num_tickets:
            self.event.available_seats -= self.num_tickets
            self.total_cost = self.calculate_booking_cost()
            print("✅ Booking successful!")
            return True
        else:
            print("❌ Not enough seats available!")
            return False

    def cancel_booking(self):
        if self.num_tickets <= self.event.total_seats - self.event.available_seats:
            self.event.available_seats += self.num_tickets
            print("✅ Booking canceled successfully!")
            return True
        else:
            print("❌ Cannot cancel more tickets than booked!")
            return False

    def getAvailableNoOfTickets(self):
        return self.event.available_seats

    def getEventDetails(self):
        return self.event