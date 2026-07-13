# 5. Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train number {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train number: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train number: {self.trainNo} from {fro} to {to} is Rs.{randint(200, 5000)}")

t = Train(12345)
t.book("Jaipur", "Delhi")
t.getStatus()
t.getFare("Jaipur", "Delhi")