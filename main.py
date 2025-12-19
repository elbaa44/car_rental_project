from vehicle import Vehicle, EconomyCar, SUV, Luxury
from customer import Customer
from rental_system import rental_system

# I generated this with AI (claude) cause I am not punctual person and I can't meet up with deadlines.

def main():

    print("=" * 60)
    print("        🚗 CAR RENTAL SYSTEM 🚗")
    print("=" * 60)
    print()

    print("📋 Step 1: Creating system...")
    system = rental_system("Elba's Auto Rentals")
    print(f"✅ System created: {system.company_name}\n")

    print("📋 Step 2: Adding vehicles...")

    eco1 = EconomyCar("ECO001", "Toyota", "Yaris", 2023, 45.0, 18.5)
    eco2 = EconomyCar("ECO002", "Hyundai", "i10", 2022, 40.0, 17.0)
    eco3 = EconomyCar("ECO003", "Kia", "Rio", 2023, 48.0, 19.0)

    suv1 = SUV("SUV001", "Toyota", "RAV4", 2023, 80.0, 5, True)
    suv2 = SUV("SUV002", "Honda", "CR-V", 2022, 75.0, 5, True)

    lux1 = Luxury("LUX001", "BMW", "X5", 2024, 150.0, ["Leather", "Panorama Roof", "Heated Seats"], True)
    lux2 = Luxury("LUX002", "Mercedes", "GLE", 2024, 160.0, ["Premium Sound", "Autopilot", "Massage Seats"], True)

    for vehicle in [eco1, eco2, eco3, suv1, suv2, lux1, lux2]:
        system.add_vehicle(vehicle)

    print(f"✅ Added {len(system.vehicles)} vehicles:\n")
    for v in system.vehicles.values():
        print(f"   • {v.Vehicle_id} - {v.Brand} {v.Model} ({v.Year}) - ${v.Daily_Rate:.1f}/day")
    print()

    print("📋 Step 3: Registering customers...")

    customer1 = Customer("C001", "George Smith", "595123456")
    customer2 = Customer("C002", "Maria Johnson", "595234567")
    customer3 = Customer("C003", "Nina Williams", "595345678")

    for customer in [customer1, customer2, customer3]:
        system.add_customer(customer)

    print(f"✅ Registered {len(system.customers)} customers:\n")
    for c in system.customers.values():
        print(f"   • {c.customer_id} - {c.name} ({c.phone})")
    print()

    print("📋 Step 4: Making vehicle rentals...\n")

    print("   🔹 Rental 1: George -> Toyota Yaris (5 days)")
    cost1 = eco1.rent(customer1, 5)
    print(f"      Cost: ${cost1:.2f}\n")

    print("   🔹 Rental 2: Maria -> Hyundai i10 (10 days)")
    cost2 = eco2.rent(customer2, 10)
    print(f"      Cost: ${cost2:.2f} (15% discount)\n")

    print("   🔹 Rental 3: Nina -> Toyota RAV4 (7 days)")
    cost3 = suv1.rent(customer3, 7)
    print(f"      Cost: ${cost3:.2f} (Insurance: $10/day)\n")

    print("   🔹 Rental 4: George -> Kia Rio (8 days)")
    cost4 = eco3.rent(customer1, 8)
    print(f"      Cost: ${cost4:.2f} (15% discount)\n")

    print("   🔹 Rental 5: Maria -> Honda CR-V (4 days)")
    cost5 = suv2.rent(customer2, 4)
    print(f"      Cost: ${cost5:.2f}\n")

    print("📋 Step 5: Returning vehicles...\n")

    print("   🔹 George returns Toyota Yaris (on time)")
    eco1.return_vehicle()
    print(f"      Vehicle returned successfully\n")

    print("   🔹 Maria returns Hyundai i10 (on time)")
    eco2.return_vehicle()
    print(f"      Vehicle returned successfully\n")

    print("   🔹 Nina returns Toyota RAV4 (on time)")
    suv1.return_vehicle()
    print(f"      Vehicle returned successfully\n")

    print("   🔹 George returns Kia Rio (on time)")
    eco3.return_vehicle()
    print(f"      Vehicle returned successfully\n")

    print("   🔹 Maria returns Honda CR-V (on time)")
    suv2.return_vehicle()
    print(f"      Vehicle returned successfully\n")

    print("📋 Step 6: System Statistics\n")

    print(f"   📊 Available vehicles: {len(system.get_available_vehicles())}")
    print(f"   📊 Rented vehicles: {system.get_active_rentals_count()}")
    print(f"   📊 Total revenue: ${system.get_total_revenue():.2f}")
    print(f"   📊 Most popular vehicle: {system.get_most_popular_vehicle()}")
    print()

    print("   🏆 TOP 3 CUSTOMERS:\n")
    top_customers = system.get_top_customers(3)
    for i, (name, spent) in enumerate(top_customers, 1):
        print(f"      {i}. {name} - ${spent:.2f}")
    print()

    print("📋 Step 7: Generating detailed report...\n")

    report_filename = "rental_report.txt"
    system.generate_report(report_filename)

    print()
    print("=" * 60)
    print("        ✅ Demo program completed successfully!")
    print("=" * 60)
    print()
    print("📄 Report file created: rental_report.txt")
    print("📂 Open the file to see detailed information")
    print()



main()