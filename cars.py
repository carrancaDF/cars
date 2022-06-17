cars = 100
space_in_a_car = 4.0 
drivers = 30 
passengers = 90 
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
avarage_passengers_per_car = passengers / cars_driven 

#Várias variáveis para fazer contas e treinar f strings e operações matemáticas com variáveis.
#Descrições e operações com variáveis e print. 

print("===========================* C * A * R * S *==========================")
print(f"There are {cars} cars available.")
print(f"There are only {drivers} drivers available.")
print(f"There will be {cars_not_driven} empty cars today.")
print(f"We can transport {carpool_capacity} people today.")
print(f"We have {passengers} to carpool today.")
print(f"We need to put about {avarage_passengers_per_car} in each car.")
print("===========================* C * A * R * S *==========================")


