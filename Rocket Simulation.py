import numpy as np
import pylab as pl

#here we prompt for all necessary imput variables
initial_mass = input("Please enter the total initial mass of the rocket and fuel in kilograms.")
percent_fuel = input("Please enter the percent of the total mass that is initially fuel.")
exhaust_speed = input("Please enter the relative speed of the exhaust gases to the rocket in meters per second.")
mass_loss_rate = input("Please enter the rate at which the mass of the rocket is changing in kilograms per second.")

#behind the scenes conversions
initial_mass = float(initial_mass)
percent_fuel = float(percent_fuel)/100
exhaust_speed = float(exhaust_speed)
mass_loss_rate = float(exhaust_speed)

#here we do calculate for the final speed
fuel_mass = initial_mass - (percent_fuel*initial_mass)
final_mass = initial_mass - fuel_mass
burn_time = fuel_mass/mass_loss_rate
thrust = exhaust_speed*mass_loss_rate
final_speed = -1*(exhaust_speed*np.log(initial_mass/final_mass) - (9.8*burn_time))
print("The final speed of the rocket is ", final_speed," meters per second.")

#here we prepare the set of coordinates for the speed of the rocket as a function of time
x = [ ]
y = [ ]

#this loop uses a timer variable that increments every second. once the timer gets up to the toal burn time, the loop is exited.
#within the loop, the time of the timer is added to the x-array. the speed of the rocket at the timer's time is calculated and added to the y-array. 
timer = 0
while (timer < burn_time):
    current_mass = initial_mass - (mass_loss_rate*timer)
    speed = -1*(exhaust_speed*np.log(initial_mass/current_mass) - (9.8*timer))
    x.append(timer)
    y.append(speed)
    timer = timer + 1

#here we graph the coordinates
pl.plot(x,y,'ro')
pl.xlabel("Time (s)")
pl.ylabel("Speed (m/s)")
pl.suptitle("Speed of Rocket over Time")
pl.show()
