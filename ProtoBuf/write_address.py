#!/usr/bin/python

import addressbook_pb2
import sys

def PromptForAddress(person):
    person.id = int(input("Enter person ID number:"))
    person.name = input("Enter name:")

    email = input("Enter email address (blank for none):")
    if email != "":
        person.email = email

    while True:
        number = input("Enter a phone number(or leave blank to finish):")
        if number == "":
            break

        phone_number = person.phone.add()
        phone_number.number = number

        type = input("is this a mobile, home, or work phone?")
        if type == "mobile":
            phone_number.type = addressbook_pb2.Person.MOBILE
        elif type == "home":
            phone_number.type = addressbook_pb2.Person.HOME
        elif type == "work":
            phone_number.type = addressbook_pb2.Person.WORK
        else:
            print ("Unknown phone type, leaving as default value")


if len(sys.argv) != 2:
    print ("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
    sys.exit(-1)

address_book = addressbook_pb2.AddressBook()

try:
    f = open(sys.argv[1], "rb")
    address_book.ParseFromString(f.read())
    f.close()
except IOError:
    print (sys.argv[1] + ": Could not open file. Creating a new one.")

PromptForAddress(address_book.person.add())

f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
             
