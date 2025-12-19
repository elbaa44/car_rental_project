class Vehicle:
    _vehicle_Counter = int(0)

    def __init__(self, vehicle_id:str , brand:str , model:str , year:int , daily_rate:float , is_available:bool):
      # Trying Error Handling
        # if not isinstance(year,int) or year <= 0:
        #     raise ValueError("Year must integer and be greater than 0")
        # if daily_rate <= 0:
        #     raise ValueError("Daily Rate must be greater than 0")

        self.Vehicle_id = vehicle_id
        self.Brand = brand
        self.Model = model
        self.Year = year
        self.Daily_Rate = daily_rate
        self.is_available : bool = True

    def return_vehicle(self):
        pass


    def calculate_rental_cost(self, days:int) -> float:
        return self.Daily_Rate * self.days

    def rent(self) -> bool:
        return self.is_available

    def return_vehicle(self) -> None:
        self.is_available = True

    def get_info(self) -> str:
        status = "Available" if self.is_available else "Not Available"
        return (
            f"Vehicle ID: {self.Vehicle_id} | {self.brand} {self.model} ({self.year})\n"
            f"Price: {self.calculate_rental_cost()} {status}\n"
        )



    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({year})"

class  EconomyCar(Vehicle):
    _economy_counter = int(0)

    def __init__(self, brand:str, model:str, year:int, daily_rate:float, fuel_efficiency:float):
        super().__init__(self, brand, model, year)
        self.daily_rate = daily_rate
        self.brand = brand
        self.model = model
        self.fuel_efficiency = fuel_efficiency
        EconomyCar._economy_counter += 1

    def calculate_rental_cost(self, days:int) -> float:
        fee = self.daily_rate * days
        if days >= 7:
            return fee * 0.85
        return fee

    def get_fuel_info(self) -> str:
        return f"Fuel efficiency: {self.fuel_efficiency}"



class SUV(Vehicle):
    _suv_counter = int(0)
    def __init__(self, brand:str, model:str, year:int, daily_rate:float , seats:int , has_4wd:bool):

        super().__init__(self, brand, model, year)
        self.daily_rate = daily_rate
        self.brand = brand
        self.model = model
        self.year = year
        SUV._suv_counter = SUV._suv_counter + 1
        self.seats = seats
        self.has_4wd = True

    def calculate_rental_cost(self, days:int) -> float:
        return (self.daily_rate + 10) * days

    def  get_capacity_info(self) -> str:
        if self.has_4wd:
          return f"Seats: {self.seats} , 4wd : ✔️"
        if self.has_4wd == False:
          return f"Seats: {self.seats} , 4wd : ❌"

class Luxury(Vehicle):
    _luxury_counter = int(0)

    def __init__(self , brand:str , model:str , year:int, daily_rate:float, features:list , requires_deposit:bool):
        super().__init__(self, brand, model, year,daily_rate)

        self.brand = brand
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.features = []
        self.requires_deposit = True

    def calculate_rental_cost(self, days:int) -> float:
        return (self.daily_rate) * days

    def requires_deposit(self , deposit) -> float:
        deposit = self.daily_rate * 3
        return deposit














        




















