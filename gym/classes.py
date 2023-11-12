class GroupExercise:
    # Constructor to initialize the GroupExercise object
    def __init__(self, name, max_capacity, fee):
        self.__name = name
        self.__trainer = None
        self.__max_capacity = max_capacity
        self.__participants = []
        self.__waitlist = []
        self.__fee = fee
        self.__checked_in_members = []

    # Getter method for the name of the group exercise
    def get_name(self):
        return self.__name

    # Getter and setter methods for the trainer assigned to the group exercise
    def get_trainer(self):
        return self.__trainer

    def set_trainer(self, trainer):
        self.__trainer = trainer

    # Getter method for the maximum capacity of the group exercise
    def get_max_capacity(self):
        return self.__max_capacity

    # Getter methods for the lists of participants, waitlist, fee, and checked-in members
    
    def get_participants(self):
        return self.__participants

    def get_waitlist(self):
        return self.__waitlist

    def get_fee(self):
        return self.__fee

    # Setter method for setting the class fee
    def set_fee(self, fee):
        self.__fee = fee

    # Getter method for the list of checked-in members
    def get_checked_in_members(self):
        return self.__checked_in_members

    # Method to enroll a member in the group exercise
    def enroll_member(self, member):
        if len(self.__participants) < self.__max_capacity:
            self.__participants.append(member)
        else:
            self.__waitlist.append(member)

    # Method to remove a member from enrolled participants or waitlist
    def remove_member(self, member):
        if member in self.__participants:
            self.__participants.remove(member)
            
            # Check if there are participants on the waitlist
            if self.__waitlist:
                # Move the first participant from waitlist to enrolled
                new_participant = self.__waitlist.pop(0)
                self.__participants.append(new_participant)
                print(f"Participant {new_participant.get_full_name()} moved from waitlist to enrolled.")

        elif member in self.__waitlist:
            self.__waitlist.remove(member)
        else:
            print("Member not found in the enrolled or waitlist.")


    # Method to display enrolled members
    def display_enrolled_members(self):
        print("Enrolled Members:")
        for member in self.__participants:
            print(member.get_full_name())

    # Method to display members on the waitlist
    def display_waitlist(self):
        print("Waitlisted Members:")
        for member in self.__waitlist:
            print(member.get_full_name())

    # Method to get the count of enrolled participants
    def get_enrolled_count(self):
        return len(self.__participants)

    # Method to get the count of members on the waitlist
    def get_waitlist_count(self):
        return len(self.__waitlist)

    # Method to calculate and return the available slots for enrollment
    def get_available_slots(self):
        return self.__max_capacity - len(self.__participants)

    # Method to calculate and return the total payment received for the class
    def calculate_total_payment(self):
        return self.__fee * len(self.__participants)

    # Method to mark a member's attendance
    def mark_attendance(self, member):
        if member in self.__participants:
            self.__checked_in_members.append(member)
        else:
            print("Member not enrolled in the class.")

    # Method to get the count of attendees
    def get_attendee_count(self):
        return len(self.__checked_in_members)

    # Method to calculate and return the attendance percentage
    def calculate_attendance_percentage(self):
        total_enrolled = len(self.__participants)
        if total_enrolled == 0:
            return 0.0
        return len(self.__checked_in_members) / total_enrolled * 100

    # Method to generate a string representation of the GroupExercise object
    def __str__(self):
        return f"Group Exercise: {self.__name}, Trainer: {self.__trainer.get_full_name() if self.__trainer else 'Not Assigned'}, Enrolled: {len(self.__participants)}, Waitlisted: {len(self.__waitlist)}"
    
class Member:
    # Class-level variable to track the next available membership number
    next_membership_number = 1

    def __init__(self, full_name):
        self.__full_name = full_name
        self.__membership_number = "M" + str(Member.next_membership_number).zfill(3)
        Member.next_membership_number += 1
        self.__enrolled_classes = []

    # Getter methods for full name and membership number
    def get_full_name(self):
        return self.__full_name

    def get_membership_number(self):
        return self.__membership_number

    # Getter method for the list of enrolled classes
    def get_enrolled_classes(self):
        return self.__enrolled_classes

    # Method to book a class for enrollment
    def book_class(self, group_exercise):
        if group_exercise.get_available_slots() > 0:
            self.__enrolled_classes.append(group_exercise)
            group_exercise.enroll_member(self)
        else:
            self.__waitlist.append(group_exercise)
            print("Class is full. Booking added to waitlist.")

    # Method to cancel enrollment in a class
    def cancel_enrollment(self, group_exercise):
        if group_exercise in self.__enrolled_classes:
            self.__enrolled_classes.remove(group_exercise)
            group_exercise.remove_member(self)
        elif group_exercise in self.__enrolled_classes:
            self.__enrolled_classes.remove(group_exercise)
            group_exercise.remove_waitlist(self)
        else:
            print("You are not enrolled in this class.")

    # Method to display enrolled classes
    def display_enrolled_classes(self):
        print("Enrolled Classes:")
        for class_obj in self.__enrolled_classes:
            print(class_obj.get_name())

    # Method to generate a string representation of the Member object
    def __str__(self):
        return f"Member: {self.__full_name}, Membership Number: {self.__membership_number}"

class Trainer:
    def __init__(self, full_name, specialization):
        # Constructor to initialize the Trainer object
        self.__full_name = full_name
        self.__specialization = specialization
        self.__assigned_classes = []

    # Getter methods for full name and specialization
    def get_full_name(self):
        return self.__full_name

    def get_specialization(self):
        return self.__specialization

    # Method to display assigned classes
    def display_assigned_classes(self):
        print("Assigned Classes:")
        for class_obj in self.__assigned_classes:
            print(class_obj.get_name())

    # Method to add a class to the list of assigned classes
    def add_assigned_class(self, group_exercise):
        self.__assigned_classes.append(group_exercise)
        group_exercise.set_trainer(self)

    # Method to generate a string representation of the Trainer object
    def __str__(self):
        return f"Trainer: {self.__full_name}, Specialization: {self.__specialization}"
