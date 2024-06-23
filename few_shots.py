few_shots = [
    {
        'Question': "How many automatic cars do we have under 20k mileage?",
        'SQLQuery': "SELECT COUNT(*) FROM cars WHERE transmission = 'Automatic' AND mileage < 20000",
        'SQLResult': "Result of the SQL Query",
        'Answer': "10"
    },
    {
        'Question': "How much money have we already collected from renting car number 1?",
        'SQLQuery': "SELECT SUM(amount_paid) AS `money_collected` FROM payments WHERE rental_id IN (SELECT rental_id FROM rentals WHERE car_id=1)",
        'SQLResult': "Result of the SQL Query",
        'Answer': "320.00"
    },
    {
        'Question': "What car is the most expensive per day to rent?",
        'SQLQuery': "SELECT brand, model, price_per_day FROM cars ORDER BY price_per_day DESC LIMIT 1",
        'SQLResult': "Result of the SQL Query",
        'Answer': "Tesla Model S"
    },
    {
        'Question': "How many successful rented transactions and how much money have we earned?",
        'SQLQuery': "SELECT COUNT(*) AS `successful_rents`, SUM(`total_cost`) AS `money_earned` FROM `rentals` WHERE `rental_end_date` IS NOT NULL",
        'SQLResult': "Result of the SQL Query",
        'Answer': "3180.00"
    },
    {
        'Question': "Which brands have cars that have been rented more than once?",
        'SQLQuery': "SELECT c.brand, COUNT(r.car_id) AS rental_count FROM rentals r JOIN cars c ON r.car_id = c.car_id GROUP BY c.brand ORDER BY rental_count DESC LIMIT 4",
        'SQLResult': "Result of the SQL Query",
        'Answer': "Toyota, Honda, Chevrolet, Ford"
    }
]
