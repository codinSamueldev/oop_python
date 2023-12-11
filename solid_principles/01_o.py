"""
OCP (Open/Closed Principle)
Objects or entities should be open for extension but closed for modification.
This means that a class should be extendable without modifying the class itself.
"""

class Notification:
    def __init__(self, user, message):
        self.user = user
        self.message = message

    
    def notify(self):
        raise NotImplementedError
    

class EmailNotification(Notification):
    def notify(self):
        return f"Sending email to {self.user.email}"
    

class WhatsAppNotification(Notification):
    def notify(self):
        return f"Sending SMS to {self.user.sms}"
    

class SMSNotification(Notification):
    def notify(self):
        return f"Sending WhatsApp text to {self.user.whatsapp}"