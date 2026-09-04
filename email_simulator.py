import datetime

class Email:
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.read_status = False
        self.timestamp = datetime.datetime.now()

    def update_read_status(self):
        self.read_status = True

    def show_email(self):
        self.update_read_status()
        print("\n*-----Email-----*\n")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")
        print(f"Date: {self.timestamp.strftime('%Y-%m-%d')}  Time: {self.timestamp.strftime('%H:%M')}")
        print("\n*---------------*")

    def __str__ (self):
        current_status = "Read" if self.read_status else "Unread"
        return f"{current_status} | From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%H:%M')}"


class User:
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()

    def send_email(self, receiver, subject, body):
        email = Email(sender = self, receiver = receiver, subject = subject, body = body)
        receiver.inbox.save_email(email)
        print(f"\nEmail send successfully from {self.name} to {receiver.name}")

    def check_inbox(self):
        print(f"\n{self.name}'s Inbox")
        self.inbox.check_inbox() 

    def read_email(self, index):
        self.inbox.read_email(index)

    def delete_email(self, index):
        self.inbox.delete_email(index)
        
    
class Inbox:
    def __init__ (self):
        self.emails = []


    def save_email(self, email):
        self.emails.append(email)


    def check_inbox(self):
        if not self.emails:
            print("Empty Inbox!")
            return
        
        for numbering, individual_email in enumerate(self.emails, start = 1):
            print(f"\n{numbering}. {individual_email}")
        else:
            print("--------------")


    def read_email(self, index):
        if not self.emails:
            print("Empty Inbox!")
            return
        
        original_index = index - 1
        if original_index < 0 or original_index >= len(self.emails):
            print("Invalid Index Number...")
            return
        self.emails[original_index].show_email()


    def delete_email(self, index):
        if not self.emails:
            print("Empty Inbox!")
            return
        
        original_index = index - 1
        if original_index < 0 or original_index >= len(self.emails):
            print("Invalid Index Number...")
            return
        del self.emails[original_index]



zaryab = User("Zaryab")  # Sender
ali = User("Ali")        # Receiver
zaryab.send_email(ali, "Hello", "Hey! ali, what's up dude?")     # Sending message to 'Ali'
ali.check_inbox()
ali.read_email(1)

ahmed = User("Ahmed")   # Sender
ahmed.send_email(ali, "Tomorrow Plan", "Do you remember that we have to go to the market tomorrow?")  # Sending message to 'Ali'
ali.check_inbox()

ali.send_email(zaryab, "Hy", "Hello Zaryab! I am fine.\nWhat's going on?")  # Ali send message back to Zaryab
zaryab.check_inbox()







    
