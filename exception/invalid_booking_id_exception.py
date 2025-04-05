class InvalidBookingIDException(Exception):
    def __init__(self, message="❌ Invalid booking ID. Please check and try again."):
        self.message = message
        super().__init__(self.message)
