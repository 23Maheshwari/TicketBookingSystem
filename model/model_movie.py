from model_event import Event

class Movie(Event):
    def __init__(self, event_id, event_name, event_venue, event_date, event_time, ticket_price, total_seats, available_seats, genre, actor_name, actress_name):
        super().__init__(event_id, event_name, event_venue, event_date, event_time, ticket_price, "Movie", total_seats, available_seats)
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_info(self):
        print(f"🎬 Movie: {self.event_name} at {self.event_venue} on {self.event_date} at {self.event_time}")
        print(f"Ticket Price: ₹{self.ticket_price} | Total Seats: {self.total_seats} | Available: {self.available_seats}")
        print(f"Genre: {self.genre} | Actor: {self.actor_name} | Actress: {self.actress_name}")