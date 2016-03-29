#! /usr/bin/python
# _*_coding: utf-8

import os

# Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Floria': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Create a basic set of states and some cities in them
Cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonvill'
}

# Add some more cities
Cities['NY'] = 'New York'
Cities['OR'] = 'Portland'

# Print out some cities
print '_' * 50
print 'NY state has:', Cities['NY']
print 'OR state has:', Cities['OR']

# Print out some states
print '_' * 50
print 'Michigen \'s abbreviation is: ', states['Michigan']
print 'Florida \'s abbreviation is: ', states['Floria']

#do it by using the state then city dict
print '_' * 50
for state, abbrev in states.items():
    print '%s is abbreviated %s' % (state, abbrev)

# print every city in state
for abbrev, city in Cities.items():
    print '%s has the city %s' % (abbrev, city)

# now do both at the sometime
for state, abbrev in states.items():
    print '%s state is abbreviated %s and has city %s' % (state, abbrev, Cities[abbrev])

print '_' * 50
# Safely get abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print 'Sorry, no Texas.'

# get a city with a default value
city = Cities.get('TX', 'Do not Exist')
print "The city for the state 'TX' is: %s" % city