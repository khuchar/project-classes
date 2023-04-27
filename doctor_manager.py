class DoctorManager:

    # create a list of doctors and populate it from the doctors.txt
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    # format doctor object just like in the file
    def format_dr_info(self, dr):
        return f"{dr.get_doctor_id()}_{dr.get_name()}_{dr.get_specialization()}_" \
               f"{dr.get_working_time()}_{dr.get_qualification()}_{dr.get_room_number()}"

    # ask user for info to enter new doctor
    def enter_dr_info(self):
        dr_id = input("Enter the doctor’s ID: ")
        name = input("Enter the doctor’s name: ")
        specialization = input("Enter the doctor’s specility: ")
        working_time = input("Enter the doctor’s timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor’s qualification: ")
        room_number = input("Enter the doctor’s room number: ")
        print()
        new_doctor = Doctor(dr_id, name, specialization, working_time, qualification, room_number)
        return new_doctor

    # reads doctors.txt to get a list of doctors. This file is separated by underscores
    def read_doctors_file(self):
        with open("doctors.txt") as f:
            # skip the header line
            next(f)
            for line in f:
                parts = line.strip().split("_")
                self.doctors.append(Doctor(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))


    # search for a doctor in the doctors list by id. If it is found print it
    def search_doctor_by_id(self):
        dr_id = input("Enter the doctor Id: ")
        found = False
        for dr in self.doctors:
            if dr.get_doctor_id() == dr_id:
                print("{:<10} {:<20} {:<15} {:<15} {:<15} {:<10}\n".format(
                    "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                print(self.display_doctor_info(dr))
                found = True
                break
        if not found:
            print("Can't find the doctor with the same ID on the system\n")

    # search for a doctor in the doctors list by name. If it is found print it
    def search_doctor_by_name(self):
        name = input("Enter the doctor name: ")
        found = False
        for dr in self.doctors:
            if dr.get_name() == name:
                print("{:<10} {:<20} {:<15} {:<15} {:<15} {:<10}\n".format(
                    "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))
                print(self.display_doctor_info(dr))
                found = True
        if not found:
            print("Can't find the doctor with the same name on the system\n")

    # display one doctor object in fixed width fields like a table
    def display_doctor_info(self, dr):
        return "{:<10} {:<20} {:<15} {:<15} {:<15} {:<10}\n".format(
            dr.get_doctor_id(), dr.get_name(), dr.get_specialization(), dr.get_working_time(), dr.get_qualification(),
            dr.get_room_number())

    # edit the doctor in the doctors list and also update the doctors.txt file
    def edit_doctor_info(self):
        dr_id = input("Please enter the id of the doctor that you want to edit their information: ")
        for dr in self.doctors:
            if dr.get_doctor_id() == dr_id:
                dr.set_name(input("Enter new Name: "))
                dr.set_specialization(input("Enter new Specilist in: "))
                dr.set_working_time(input("Enter new Timing: "))
                dr.set_qualification(input("Enter new Qualification: "))
                dr.set_room_number(input("Enter new Room number: "))
                print()
                self.write_list_of_doctors_to_file()
                print(f"Doctor whose ID is {dr_id} has been edited\n")
                return
        print("Can't find the doctor with the same ID on the system\n")

    # displays a list of doctors by calling the display_doctor_info in a loop
    def display_doctors_list(self):
        print("{:<10} {:<20} {:<15} {:<15} {:<15} {:<10}\n".format(
            "Id", "Name", "Speciality", "Timing", "Qualification", "Room Number"))

        for dr in self.doctors:
            print(self.display_doctor_info(dr))

    # writes list of doctors to the file. Gets formatted line from format_dr_info() and writes each line
    def write_list_of_doctors_to_file(self):
        with open("doctors.txt", "w") as f:
            for dr in self.doctors:
                f.write("\n" + self.format_dr_info(dr))

    # appends new doctors to the end of file
    def add_dr_to_file(self):
        new_dr = self.enter_dr_info()
        self.doctors.append(new_dr)
        with open("doctors.txt", "a") as f:
            f.write(self.format_dr_info(new_dr) + "\n")
        print(f"Doctor whose ID is {new_dr.get_doctor_id()} has been added\n")
