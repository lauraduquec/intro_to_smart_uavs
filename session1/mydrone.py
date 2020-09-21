from drones import Drone

fuel = <fuel>
max_speed = <max_speed>
refuel_quantity = <refuel_quantity>
drone = Drone(fuel, max_speed)


print('Current fuel is ' +str(drone.get_fuel()))
print('Current speed is ' +str(drone.get_speed()))
drone.add_fuel(refuel_quantity)
print('Now the fuel is ' +str(drone.get_fuel()))
drone.set_speed(<new_speed>)
print('Current speed is ' +str(drone.get_speed()))
drone.fly()
