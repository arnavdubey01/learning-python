# 6. Can you change the slf-parameter inside a class to something else (say “harry”)? Try changing slf to “slf” or “harry” and see the effects


from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train number {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train number: {slf.trainNo} is running on time")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train number: {slf.trainNo} from {fro} to {to} is Rs.{randint(200, 5000)}")

t = Train(12345)
t.book("Jaipur", "Delhi")
t.getStatus()
t.getFare("Jaipur", "Delhi")

#So, nothing changes. But still 'self' is preferred as anything else affects readability.
# Like why would anyone replace 'self' with 'harry'