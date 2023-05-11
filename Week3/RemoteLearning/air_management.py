# Your goal is to build an airplanes traffic management system.
#
# Details
# Your program should rely on four classes: Airline, Airplane, Flight and Airport.
#
# Consider every plane can fly only once per day.
#
# The Airline Class
# Attributes:
#
# flight_id (str) A two letters code
# name (str)
# planes : A list of Airplanes belonging to this airline (see below the Airplane class)
# This class has no methods
#
# The Airplane Class
# Attributes:
#
# flight_id (int)
# current_location : The Airport where the airplane is currently located (see below the Airport class)
# company : The airline this airplane belongs to (see above the Airline class)
# next_flights : The list of Flights. Every future flights of the airplane, this list should always be sorted by datetime. (see below the Flight class)
#
# Methods:
#
# fly(self, destination)
# location_on_date(self, date): Returns where the plane will be on this date
# available_on_date(self, date, location) : Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).
#
# The Flight Class
# Attributes:
#
# date (datetime.Date)
# destination : The destination airport. (see below the Airport class)
# origin : The departure airport. (see below the Airport class)
# plane : The plane used during this flight. (see above the Airplane class)
# flight_id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.
# Methods:
#
# Those methods are here only to update the rest of the system, for example, to change the location of the plane when it reaches its destination:
#
# take_off(self)
# land(self)
#
# The Airport Class
# Attributes:
#
# city (str) The code of the city where the airport is located
# planes : The list of every plane that is currently in this airport. (see above the Airplane class)
# scheduled_departures : The list of flight - Every future flight from this airport, sorted by date. (see above the Flight class)
# scheduled_arrivals : The list of flight - Every future flight that will arrive to this airport, sorted by date. (see above the Flight class)
#
# Methods:
#
# schedule_flight(self, destination, datetime) :
# finds an available airplane from an airline, that serves the departure and the destination
# schedule the airplane for the flight
# info(self, start_date, end_date) : Displays every scheduled flight from start_date to end_date.
#
# You are free to add any class/method/attribute to your code, be sure to document everything you write.
#
# Write a small code to test your program.

import string
from faker import Faker
from faker_airtravel import AirTravelProvider
from faker.providers import BaseProvider
import datetime
import random

NUM_OF_AIRLINES = 5
NUM_OF_AIRPORTS = 50
NUM_OF_PLANES = 500
NUM_OF_FLIGHTS = 50_000

NUM_DAYS = 200
BASE = datetime.datetime.today().date()
DATES_LIST = [BASE + datetime.timedelta(days=x) for x in range(NUM_DAYS)]


class AirlineCodeProvider(BaseProvider):
    def airline_code(self) -> str:
        return random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)


class Airline:

    AIRLINES = list()

    def __init__(self, airline_id: str, name: str):
        self.airline_id = airline_id
        self.name = name
        self.planes = list()
        self.AIRLINES.append(self)


class Airport:

    AIRPORTS = list()

    def __init__(self, city: str):
        self.city = city
        self.planes = list()
        self.scheduled_departures = list()
        self.scheduled_arrivals = list()
        self.AIRPORTS.append(self)

    def schedule_flight(self, destination, date_time: datetime.date):
        for plane in self.planes:
            if plane.available_on_date(date_time, self):
                flight_id = f"{destination.city} - {plane.airplane_id} - {str(date_time)}"
                flight = Flight(date_time, destination, self, plane, flight_id)
                plane.next_flights.append(Flight(date_time, destination, self, plane, flight_id))
                plane.next_flights.sort(key=lambda x: x.date)

                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)

    def info(self, start_date, end_date):
        print("Scheduled Departures:")
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"{flight.date} - {flight.destination.city} - {flight.plane.airplane_id} - {flight.flight_id}")

        print("\nScheduled Arrivals:")
        for flight in self.scheduled_arrivals:
            if start_date <= flight.date <= end_date:
                print(f"{flight.date} - {flight.destination.city} - {flight.plane.airplane_id} - {flight.flight_id}")


class Airplane:

    AIRPLANES = list()

    def __init__(self, airplane_id: int, current_location: Airport, company: Airline):
        self.airplane_id = airplane_id
        self.current_location = current_location
        self.company = company
        self.next_flights = list()
        self.AIRPLANES.append(self)

    def fly(self, destination: Airport):
        self.next_flights[0].take_off(destination, self)
        self.next_flights[0].land(destination, self)

    def location_on_date(self, date: datetime.date):
        for next_flight in self.next_flights:
            if next_flight.date == date:
                return next_flight.destination

    def available_on_date(self, date: datetime.date, location: Airport):
        for flight in self.next_flights:
            if flight.date == date:
                return False

        # FIND THE LAST LOCATION ON THE CLOSEST PREVIOUS DATE
        flights = [flight for flight in self.next_flights if flight.date <= date]
        flights.sort(key=lambda x: x.date)

        if len(flights) > 0:
            if flights[-1].destination == location:
                return True
        else:
            return True


class Flight:

    FLIGHTS = list()

    def __init__(self, date: datetime.date, destination: Airport, origin: Airport, plane: Airplane, flight_id: str):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.flight_id = flight_id
        self.FLIGHTS.append(self)

    def take_off(self, airport: Airport, plane: Airplane):
        airport.scheduled_departures.remove(self)
        airport.planes.remove(plane)
        plane.current_location = "in air"

    def land(self, airport: Airport, plane: Airplane):
        plane.next_flights.remove(self)
        airport.scheduled_arrivals.remove(self)
        airport.planes.append(plane)
        plane.current_location = airport
        self.FLIGHTS.remove(self)


if __name__ == '__main__':
    fake = Faker()
    fake.add_provider(AirTravelProvider)
    fake.add_provider(AirlineCodeProvider)

    for _ in range(NUM_OF_AIRLINES):
        Airline(fake.airline_code(), fake.airline())

    for _ in range(NUM_OF_AIRPORTS):
        Airport(fake.city())

    for i in range(NUM_OF_PLANES):
        random_airport = random.choice(Airport.AIRPORTS)
        random_airline = random.choice(Airline.AIRLINES)
        new_plane = Airplane(i, random_airport, random_airline)
        random_airport.planes.append(new_plane)

    for _ in range(NUM_OF_FLIGHTS):
        random_date = random.choice(DATES_LIST)
        random_origin = random.choice(Airport.AIRPORTS)
        random_destination = random.choice(Airport.AIRPORTS)

        random_origin.schedule_flight(random_destination, random_date)

    some_airport = random.choice(Airport.AIRPORTS)

    # some_airport.info(BASE, DATES_LIST[-1])
    # print(some_airport.planes[0].next_flights)

    # [print(flight.date) for flight in some_airport.planes[0].next_flights]
    # [print(flight.destination.city) for flight in some_airport.planes[0].next_flights]
    # [print(flight.plane.airplane_id) for flight in some_airport.planes[0].next_flights]
    # print(some_airport.planes[0].current_location.city)
