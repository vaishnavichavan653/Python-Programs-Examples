class EmailNotification:
    def send(self, message):
        print("Sending email:", message)


class SMSNotification:
    def send(self, message):
        print("Sending text message:", message)


def notify(notification, message):
    notification.send(message)


notify(EmailNotification(), "Your order has shipped.")
notify(SMSNotification(), "Your order has shipped.")
