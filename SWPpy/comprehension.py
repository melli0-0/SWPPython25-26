'''
Create a list called used_cars, containing only the model names of cars that have mileage above 50,000 km.
For each such car, append "(OLD)" if it’s older than 2018, otherwise append "(USED)"

Create a set called affordable_brands containing unique car brands where the price is below 30,000.
Only include cars that are not older than 2015.

Create a dictionary called car_ratings where the key is the car’s model name,
and the value is a rating string based on the price:
"Expensive" if price > 40,000
"Fair" if 20,000 ≤ price ≤ 40,000
"Budget" otherwise

Create a one-line comprehension that lists all models of the brand BMW
that are younger than 2019 and have a price below 40,000.
'''
import string

cars = [
    {"brand": "BMW", "model": "X5", "year": 2018, "mileage": 55000, "price": 32000},
    {"brand": "Audi", "model": "A4", "year": 2016, "mileage": 87000, "price": 15000},
    {"brand": "Tesla", "model": "Model 3", "year": 2022, "mileage": 12000, "price": 48000},
    {"brand": "Ford", "model": "Focus", "year": 2015, "mileage": 110000, "price": 9000},
    {"brand": "BMW", "model": "M3", "year": 2020, "mileage": 30000, "price": 55000},
    {"brand": "Audi", "model": "Q7", "year": 2019, "mileage": 45000, "price": 40000},
]

cars_list = ['BMW', 'Audi', 'Tesla', 'BMW', 'Ford', 'Audi', 'Toyota', 'Tesla', 'Mazda']

def list_comprehension():
    used_cars = []
    long_driven = [car.get("model") for car in cars if car.get("mileage") >= 50000 ]
    for i in range(len(long_driven)):
        car_found = False
        j=0
        while not car_found:
            if cars[j].get("model") == long_driven[i]:
                car_found = True
                model = long_driven[i]
                if cars[i].get("year") < 2018:
                    used_cars.append(model+" old")
                else:
                    used_cars.append(model+" used")
            else: j+=1
    return used_cars

def set_comprehension():
    older_cars = [car for car in cars if car.get("year")<=2015]
    affordable_brands = {older_car.get("brand") for older_car in older_cars if older_car.get("price")<30000}
    return affordable_brands

def dict_comprehension():
    car_rating ={car.get("model"):
                     ("expensive" if car.get("price") > 40000
                     else "fair" if car.get("price") >= 20000
                     else "budget")
                 for car in cars}
    return car_rating

def bonus_comprehension():
    bmw = [car.get("model") for car in cars
           if ((car.get("brand") == "BMW")
           and (car.get("year") < 2019)
           and (car.get("price") < 40000))]

    return bmw

def list_to_set():
    unique = []
    # append() returns None
    # not None = True
    unique_cars = [car for car in cars_list
                   if car not in unique and not unique.append(car)]
    return unique_cars

def dict_ascii():
    #ord() returns ascii value or unicode
    ascii_dict = {char : ord(char) for char in string.ascii_lowercase}
    return ascii_dict

if __name__ == '__main__':
    print(list_comprehension())
    print(set_comprehension())
    print(dict_comprehension())
    print(bonus_comprehension())
    print(list_to_set())
    print(dict_ascii())