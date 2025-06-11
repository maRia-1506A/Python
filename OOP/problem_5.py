"""Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under BD Railways."""

from random import randint


class Train:
    def __init__(self, trainName, seatNo):
        self.trainName = trainName
        self.seatNo = seatNo

    def bookTicket(self):
        if self.seatNo > 0:
            self.seatNo -= 1
            print(
                f"Ticket is booked successfully! Available seats left: {self.seatNo}")

    def getStatus(self):
        print(f"Train: {self.trainName}")
        print(f"Available seats: {self.seatNo}")

    def fareInfo(self, fro, to, cost):
        print(
            f"The cost for {self.trainName} from {fro} to {to} is: {cost}/=")


tr = Train("Jahanabad Express", 70)
tr.getStatus()
tr.fareInfo("Dhaka", "Jashore", randint(400, 2400))
tr.bookTicket()
tr.bookTicket()
