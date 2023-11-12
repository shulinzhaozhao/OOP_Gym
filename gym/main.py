from classes import GroupExercise, Member, Trainer

def main():
    # Create 2 GroupExercise objects
    class1 = GroupExercise("Yoga Class", max_capacity=10, fee=15)
    class2 = GroupExercise("Zumba Class", max_capacity=15, fee=10)

    # Create 5 Member objects
    member1 = Member("Alice")
    member2 = Member("Bob")
    member3 = Member("Charlie")
    member4 = Member("Diana")
    member5 = Member("Eve")

    # Create 2 Trainer objects
    trainer1 = Trainer("John", specialization="Yoga Trainer")
    trainer2 = Trainer("Lisa", specialization="Zumba Trainer")

    # Assign a trainer to each group exercise class
    trainer1.add_assigned_class(class1)
    trainer2.add_assigned_class(class2)

    # Set the class fee for each group exercise class
    class1.set_fee(15)
    class2.set_fee(10)

    # Set up specific member booking for a group exercise class
    member1.book_class(class1)
    member2.book_class(class1)
    member3.book_class(class1)
    member4.book_class(class2)
    member5.book_class(class2)

    # Cancelling a specific member’s group exercise class
    member1.cancel_enrollment(class1)

    # Record a specific member checking in to a group exercise class
    class2.mark_attendance(member4)

    # Display the list of enrolled participants for a group exercise class
    print("\nEnrolled Members for", class1.get_name())
    class1.display_enrolled_members()

    # Display the waiting list for a group exercise class
    print("\nWaiting List for", class1.get_name())
    class1.display_waitlist()

    # Display the available slots for a group exercise class
    print("\nAvailable Slots for", class1.get_name(), ":", class1.get_available_slots())

    # Display the number of participants enrolled in a group exercise class
    print("\nNumber of Participants in", class1.get_name(), ":", class1.get_enrolled_count())

    # Display the number of wait list participants in a group exercise class
    print("\nNumber of Waitlist Participants in", class1.get_name(), ":", class1.get_waitlist_count())

    # Display the number of attendees for a group exercise class
    print("\nNumber of Attendees in", class1.get_name(), ":", class1.get_attendee_count())

    # Display the attendance percentage for a group exercise class
    print("\nAttendance Percentage for", class1.get_name(), ":", class1.calculate_attendance_percentage(), "%")

    # Display the total payment collected for a group exercise class
    print("\nTotal Payment for", class1.get_name(), ":", class1.calculate_total_payment())

    # Display the list of group exercise classes for which a specific member is enrolled
    print("\nClasses Enrolled by", member2.get_full_name())
    member2.display_enrolled_classes()

    # Display the list of classes offered by a particular trainer
    print("\nClasses Offered by", trainer1.get_full_name())
    trainer1.display_assigned_classes()

if __name__ == "__main__":
    main()
