from model_event import Event

class Concert(Event):
    def __init__(self, event_id, event_name, event_venue, event_date, event_time, ticket_price, total_seats, available_seats, artist_name, genre):
        super().__init__(event_id, event_name, event_venue, event_date, event_time, ticket_price, "Concert", total_seats, available_seats)
        self.artist_name = artist_name
        self.genre = genre

    def display_event_info(self):
        print(f"🎵 Concert: {self.event_name} at {self.event_venue} on {self.event_date} at {self.event_time}")
        print(f"Ticket Price: ₹{self.ticket_price} | Total Seats: {self.total_seats} | Available: {self.available_seats}")
        print(f"Artist: {self.artist_name} | Genre: {self.genre}")