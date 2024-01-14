import random
import time

class CrewMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

class Flight:
    def __init__(self, flight_number, departure, arrival, duration):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.duration = duration
        self.captain = CrewMember(f"Captain {random.choice(['John', 'Alice', 'Bob'])}", 'Captain')
        self.crew = [CrewMember(f"Co-Pilot {random.choice(['Chris', 'Diana', 'Eva'])}", 'Co-Pilot'),
                     CrewMember(f"Attendant {random.choice(['Mike', 'Sara', 'Tom'])}", 'Flight Attendant')]

def get_flight_status(flight):
    # Simulate flight status (Delayed, On Time, etc.)
    statuses = ['On Time', 'Delayed', 'Cancelled']
    return random.choice(statuses)

def display_flight_info(flight):
    print(f"Flight Number: {flight.flight_number}")
    print(f"Departure: {flight.departure}")
    print(f"Arrival: {flight.arrival}")
    print(f"Duration: {flight.duration} hours")
    print(f"Captain: {flight.captain.name}")
    print("Crew:")
    for crew_member in flight.crew:
        print(f"  - {crew_member.name} ({crew_member.role})")
    print(f"Status: {get_flight_status(flight)}\n")

def track_flight(flight_number):
    # Simulate fetching flight details from a database or API
    departure = "Airport A"
    arrival = "Airport B"
    duration = random.randint(1, 5)
    return Flight(flight_number, departure, arrival, duration)

def main():
    while True:
        flight_number = input("Enter Flight Number (or 'exit' to quit): ")
        if flight_number.lower() == 'exit':
            break

        flight = track_flight(flight_number)
        if flight:
            display_flight_info(flight)
        else:
            print(f"Flight {flight_number} not found. Please check the flight number.\n")

if __name__ == "__main__":
    main()
