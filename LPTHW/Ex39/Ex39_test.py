#! /usr/bin/python
# _*_coding: utf-8

import hashmap

# Create a mapping of state to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# Create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Francisco')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

# Add some more cities
hashmap.set(cities, 'NY', 'Some Town')
hashmap.set(cities, 'OR', 'Portland')

# Print out some cities
print '_' * 60
print "Let me play with hash key, print it out for cities:", hashmap.hash_key(cities, 'CA')
print '_' * 60

print "This is 'cities' hashmap object: ", cities
print "This is Bucket", cities[hashmap.hash_key(states, 'CA')]
print "This is we get slot:", hashmap.get_slot(cities, 'MI')
print
print '_' * 40
print "NY State has: %s" % hashmap.get(cities, 'NY')
print "OR State has: %s" % hashmap.get(cities, 'OR')

# Print out some states
print '_' * 40
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is %s" % hashmap.get(states, 'Florida')

# do it by using the state then cities dict
print '_' * 40
print "Michigan has %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

# Print every cities in state
print '_' *40
hashmap.list(cities)

# Print every state abbreviation
print '_' * 40
hashmap.list(states)

print '_' * 40
state = hashmap.get(states, 'Texas')

if not state:
    print 'Sorry, no Texas.'

# default values using ||= with nil result
# can you do this in one line?
city = hashmap.get(cities, 'TX', 'Does Not Exist')
if city is None:
    print "Sorry, There is no city in 'TX'."
else:
    print "The city for the state 'TX' is: %s" % city

