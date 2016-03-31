#! /usr/bin/python
# _*_coding: utf-8

import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' +salt

def check_password(hash_password, user_password):
    password, salt = hash_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = raw_input('Please enter a password: ')
hash_password = hash_password(new_pass)
print "The string to store in the db is: " + hash_password

old_pass = raw_input('Now enter the password again to check: ')
if check_password(hash_password, old_pass):
    print 'You enter the right password'
else:
    print 'I am sorry but the password doest not match.'