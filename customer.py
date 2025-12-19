from vehicle import Vehicle

class Customer:
    _customer_counter = int(0)
    def __init__(self , name:str , license_number:str , phone:str) -> None:
        self._customer_counter += 1
        self.name = name
        self.license_number = license_number
        self.phone = phone
        self.customer_id = f"CUST{Customer._customer_counter:03d}"
        self.current_rentals: list[tuple[str, str, int, float]] = []
        self.rental_history: list[tuple[str, str, int, float]] = []

    def rent_vehicle(self, vehicle: Vehicle, days: int, start_date: str):
        if days <=0:
            return ValueError("days cannot be negative")

        if not vehicle.is_available:
            return False

        cost = vehicle.calculate_rental_cost(days)
        self.current_rentals.append((vehicle.Vehicle_id , start_date , days , cost))

        return True

    def return_vehicle(self, vehicle: Vehicle, days_late: int = 0):
        if days_late <= 0:
            return ValueError("days_late cannot be negative")

        rental = None

        for r in self.current_rentals:
            if r[0] == vehicle.Vehicle_id :
                rental = r
                break

        if rental is None:
                return ValueError("Rental is not available")

        vehicle_id , start_date, days, original_cost = rental

        late_fee = vehicle.Daily_Rate * 1,5 * days_late
        total = original_cost + late_fee

        self.rental_history.append((vehicle.Vehicle_id , start_date , days_late, total))
        self.current_rentals.remove(rental)

        return total

    def get_current_rentals(self) -> list:
        return self.current_rentals

    def get_rental_history(self) -> str:
       return self.rental_history

    def get_total_spent(self) -> float:
        return sum(r[5] for r in self.rental_history)

    def __str__(self) -> str:
        return f"Customer: {self.name} (ID: {self.customer_id})"

