import datetime
import os

class Attendees:
    attendees_list = [] #Create list to store all attendees.

    def __init__(self, ID, name, age): #Initialise the name and age of each attendee.
        self.ID = ID
        self.name = name
        self.age = age
        Attendees.attendees_list.append(self) #Each time a new attendee object is created, it automatically gets appended into a list.

    def __str__(self):
        #return f'Name: {self.name}, Age: {self.age}' #After an object is created with this class, it can be printed in this format.
        return f'{self.name} {self.age}'
    
    def enter_attendees():
        while True:
            try:
                attendee_id_input = int(input("Please enter the attendee's id, this should be an integer value and must not be the same as another existing attendee: \n"))
                attendee_id = f'A{attendee_id_input}'
                break
            except ValueError:
                print('Attendee ID invalid. ')

        while True:
            try:
                attendee_name = input("Please enter the attendee's name: \n")
                if not attendee_name.isalpha():
                    raise ValueError("Name should contain only alphabetical characters. \n")
                break
            except ValueError as ve:
                print(ve)
            
        while True:
            try:
                attendee_age = int(input("Please enter the attendee's age: \n"))
                break
            except ValueError:
                print('Invalid age value.')
                
        new_attendee = Attendees(attendee_id, attendee_name, attendee_age)
        with open('Attendees.txt', 'a') as file:
            file.write(f'{new_attendee.ID} {new_attendee.name} {new_attendee.age}')
            file.write('\n')
            
    def update_attendees():
        delete_or_update = input("\nIf you want to delete an attendee, press 'd', if you want to update an attendee, press 'u': ")
        if delete_or_update == 'u':
            while True:
                try: 
                    update_attendee_ID = input("\nPlease enter the ID of the attendee you would like to update?: ")
                    update_attendee_index = int(input("\nPlease enter 0 to update the attendee's name or 1 to update their age: "))
                    update_to = input("\nPlease enter the value you you would like to change to: ")
                    
                    if (update_attendee_ID in attendees_dict) and (update_attendee_index<=1):
                        attendees_dict[update_attendee_ID][update_attendee_index] = update_to
                        print('\nUpdate successful.')
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")
                    
        if delete_or_update == 'd':
            while True:
                try:
                    delete_attendee_ID = input("\nPlease enter the ID of the attendee you would like to delete?: ")
                
                    if (delete_attendee_ID in attendees_dict):
                        del attendees_dict[delete_attendee_ID]
                        print('\nDeletion successful.')
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")
        
        

class Events:
    events_list = [] #Create list to store all events.

    def __init__(self, event_ID, event_name, date, location):
        self.event_ID = event_ID
        self.event_name = event_name
        self.date = date
        self.location = location
        self.event_attendees_list = [] #List for when an attendee is added to an event.
        Events.events_list.append(self) #Each time a new attendee object is created, it automatically gets appended into a list.

    def add_attendee(self, attendee):
        self.event_attendees_list.append(attendee) #A method that allows an attendee to be added to a specific event. Takes in attendee as an input.

    def event_attendees(self):
        for attendee in self.event_attendees_list: 
            print(f'Name: {attendee.name}') #Method to list out all names of attendees of each event.

    def __str__(self):
        return f'Event_ID: {self.event_ID}, Event: {self.event_name}, Date: {self.date}, Location: {self.location}' #After an object is created with this class, it can be printed in this format.

    def enter_events():
        while True:
            try:
                event_id_input = int(input("Please enter the event ID, this should be an integer value and must not be the same as another existing event: \n"))
                event_id = f'E{event_id_input}'
                break
            except ValueError:
                print('Invalid attendee ID.')

        event_name = input("Please enter the event name: \n")
        
        while True:    
            try:
                event_date = (input("Please enter the date of the event in format 'DD-MM-YY': \n"))
                date_obj = datetime.datetime.strptime(event_date, '%d-%m-%y').date()
                break
            except ValueError:
                print("Invalid date format.")
             
        event_location = input("Please enter the event location: \n")
        
        new_event = Events(event_id ,event_name ,event_date ,event_location)
        with open('Events.txt', 'a') as file:
            file.write(f'{new_event.event_ID} {new_event.event_name} {new_event.date} {new_event.location}')
            file.write('\n')

    def update_events():
        delete_or_update = input("\nIf you want to delete an attendee, press 'd', if you want to update an attendee, press 'u': ")
        if delete_or_update == 'u':
            while True:
                try: 
                    update_event_ID = input("\nPlease enter the ID of the event you would like to update?: ")
                    update_event_index = int(input("\nPlease enter 0 to update the event name, 1 to update the date or 2 to update the location: "))
                    update_to = input("\nPlease enter the value you you would like to change to: ")
                    
                    if (update_event_ID in events_dict) and (update_event_index<=2):
                        events_dict[update_event_ID][update_event_index] = update_to
                        print('\nUpdate successful.')
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")
                    
        if delete_or_update == 'd':
            while True:
                try:
                    delete_event_ID = input("\nPlease enter the ID of the event you would like to delete?: ")
                
                    if (delete_event_ID in events_dict):
                        del events_dict[delete_event_ID]
                        print('\nDeletion successful.')
                        break
                    else:
                        print("You have entered something invalid.")
                    
                except ValueError:
                    print("\nYou have entered something invalid.")

#--------------------------------------------------------------------------------------------------------------------------------------------
while True:
    event_or_attendee = input("Please type 'a' to enter in a new attendee and 'e' to enter in a new event. Or Press Enter to continue. \n")
    
    if event_or_attendee == 'a':
        Attendees.enter_attendees()

    if event_or_attendee == 'e':
        Events.enter_events()
            
    input_again = input("Would you like to enter more information? If yes, please type 'y' or press Enter to continue. \n")
    if input_again == 'y':
        continue
    else:
        break

#--------------------------------------------------------------------------------------------------------------------------------------------

attendees_dict = {}
events_dict = {}

with open('Events.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        event_id, event_name, event_date, event_location = parts
        events_dict[event_id] = [event_name, event_date, event_location]

with open('attendees.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        attendee_id, attendee_name, attendee_age = parts
        attendees_dict[attendee_id] = [attendee_name, int(attendee_age)]

print(attendees_dict)
print(events_dict)

update_info = input("\nWould you like to update or delete a record?\nPlease type 'a' for attendees or 'e' for events.\nOr press Enter if you don't want to make any changes:")
if update_info == 'a':
    Attendees.update_attendees()

if update_info == 'e':
    Events.update_events()

print(attendees_dict)
print(events_dict)     

with open('attendees.txt', 'w') as text_file:
    for key, value in attendees_dict.items():
        text_file.write(f'{key} {value[0]} {value[1]} \n')

with open('events.txt', 'w') as text_file:
    for key, value in events_dict.items():
        text_file.write(f'{key} {value[0]} {value[1]} {value[2]} \n')