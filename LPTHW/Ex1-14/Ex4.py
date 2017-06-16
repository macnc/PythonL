#!/usr/local/bin/python
# _*_coding: utf-8

# Define how many cars here
cars = 100
# Define how big space per car.
space_in_a_car = 4.0
# Define how many drivers here.
drivers = 30
# Define how many passengers here.
passengers = 90
# calculate how many cars will be no driver to drive.
cars_not_driven = cars - drivers
# Define how many cars will be driven here.
cars_driven = drivers
# calculate the cpacity of transport for passengers.
carpool_capacity = cars_driven * space_in_a_car
# calculate how many passengers will be taken by each car.
average_passengers_per_car = passengers / cars_driven


# print out how many cars here.
print "There are", cars, "cars available."
# print out how many drivers here.
print "There are only", drivers, "drivers available."
# print out how many cars will not be driven here.
print "There will be", cars_not_driven, "empty cars today."
# print out how many people will be transported here.
print "We can transport", carpool_capacity, "people today."
# print out how many passengers can be put in each car.
print "We need to put about", average_passengers_per_car, "in each car."
