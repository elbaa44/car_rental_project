🚗 Car Rental System (Python OOP Project)

A Car Rental Management System implemented in Python, demonstrating Object-Oriented Programming (OOP) principles such as inheritance, encapsulation, polymorphism, and clean project structure.

This project simulates a real-world car rental company, allowing vehicle management, customer rentals, cost calculation, penalties, and detailed report generation.

📌 Features

🚘 Manage multiple vehicle types:

Economy Cars

SUVs

Luxury Cars

👤 Customer registration and rental tracking

💰 Automatic rental cost calculation

⏱ Late return penalty handling

📊 Rental history and total spending per customer

🗂 Vehicle availability tracking

📄 Detailed report generation to .txt file

🧠 Clean OOP design with inheritance and method overriding

🧱 Project Structure
car_rental_system/
│
├── vehicles.py          # Vehicle base class + child classes
├── customer.py          # Customer logic (rentals, history, finance)
├── rental_system.py     # Main system manager
├── main.py              # Example usage & testing
└── README.md            # Project documentation

🚙 Vehicle Types
Base Class: Vehicle

Shared attributes and methods

Automatic vehicle ID generation

Availability control

EconomyCar

15% discount for rentals of 7+ days

Fuel efficiency info

SUV

Extra insurance fee: +10 GEL/day

Seat count & 4x4 support

LuxuryCar

Premium fee: +20 GEL/day

Requires deposit (3× daily rate)

Feature list (GPS, Leather Seats, etc.)

👥 Customer Management

Each customer has:

Unique ID

Active rentals

Rental history

Total money spent

Supported actions:

Rent vehicle

Return vehicle (with late fee)

View rental history

Calculate total expenses

💸 Pricing Rules
Vehicle Type	Cost Formula
Vehicle	daily_rate * days
EconomyCar	15% discount if days >= 7
SUV	(daily_rate + 10) * days
LuxuryCar	(daily_rate + 20) * days
Late Fee	daily_rate * 1.5 * days_late
Luxury Deposit	daily_rate * 3
📊 Rental System Capabilities

Add & find vehicles/customers

List available vehicles

Filter vehicles by type

Calculate total revenue

Find most popular vehicle

Generate detailed company report

📄 Report Generation

The system can generate a formatted .txt report including:

Company summary

Vehicle statistics by type

Customer statistics

Financial overview

Top 3 customers by spending

Detailed vehicle lists with status

▶️ How to Run
1️⃣ Clone the repository
git clone https://github.com/your-username/car-rental-system.git
cd car-rental-system

2️⃣ Run the demo
python main.py

🧪 Testing Individual Modules

Example (testing customer.py):

python customer.py



🛠 Technologies Used

Python 3.10+

Standard Library only

Object-Oriented Programming (OOP)

🎓 Educational Purpose

This project was created as a learning-oriented university-level assignment, focusing on:

OOP best practices

Clean architecture

Real-world logic modeling

Debugging & testing discipline

📜 License

This project is free to use for educational purposes.
