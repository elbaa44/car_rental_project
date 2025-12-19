from collections import Counter

import customer


class rental_system:
    def __init__(self, company_name: str):

        self.company_name = company_name
        self.vehicles = {}
        self.customers = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.id] = vehicle

    def add_customer(self, customer):
        self.customers[customer.id] = customer

    def find_vehicle(self, id):
        return self.vehicles[id]

    def find_customer(self, id):
        return self.customers[id]

    def get_available_vehicles(self):
        return (v for v in self.vehicles.values() if v.is_available())

    def get_vehicles_by_type(self, vehicle_type: str) -> list:
        pass

    def get_total_revenue(self) -> float:
        total_revenue = 0.0
        for c in self.customers.values():
            for rental in self.rental_history:
                total_revenue += rental['cost']

        return total_revenue

    def get_most_popular_vehicle(self):
        vehicle_ids = []
        for c in self.customers.values():
            for rental in customer.get_rental_history:
                vehicle_ids.append(rental['vehicle_id'])

        if not vehicle_ids:
            return "No rentals yet."

        counter = Counter(vehicle_ids)
        return counter.most_common(1)[0][0]

    def generate_report(self, filename: str) -> None:
        pass
