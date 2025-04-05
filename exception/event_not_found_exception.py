class EventNotFoundException(Exception):
    def __init__(self, message="❌ Event not found in the system."):
        self.message = message
        super().__init__(self.message)
