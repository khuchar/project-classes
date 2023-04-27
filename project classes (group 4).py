# Hospital Management System
#
# Author: Kevin Vuong, Charlie Khu, Tho my Nguyen
# Date: [April 25th 2023]

# This program is designed to help manage patient and doctor records for a hospital.
# The program reads patient and doctor information from text files, and allows the user
# to add and edit records. The program also provides a menu-based interface
# to display patient and doctor records, as well as search for records by ID or name.
#
# Inputs:
# - patient.txt: a text file containing patient records
# - doctor.txt: a text file containing doctor records
# - User input from the console: the user can add or edit patient and doctor records,
#   as well as display records or search for records by ID or name.
#
# Outputs:
# - The program displays patient and doctor records in a table format
# - The program allows the user to search for records by ID or name and displays the
#   corresponding records in a table format.
# - The program writes the updated patient and doctor records back to the text files.
#
# Processing:
# - The program reads patient and doctor records from text files and stores them as objects.
# - The program provides functions to add and edit patient and doctor records,
#   and writes the updated records back to the text files.
# - The program provides functions to display patient and doctor records in a table format,
#   as well as search for records by ID or name.
#


##############################################################

class Doctor:

    # in constructor keyword arguments are used so that the object can be instantiated without passing values

    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None,
                 room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # getters and setters

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_specialization(self):
        return self.specialization

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def get_working_time(self):
        return self.working_time

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    # returns string representation of doctor object with underscores in between just like in file
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

#############################################################################


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


##############################################################################


class Patient:

    # in constructor keyword arguments are used so that the object can be instantiated without passing values

    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    # getters and setters

    def get_pid(self):
        return self.pid

    def set_pid(self, new_pid):
        self.pid = new_pid

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_disease(self):
        return self.disease

    def set_disease(self, new_disease):
        self.disease = new_disease

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    # returns string representation of patient object with underscores in between just like in file
    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"


#############################################################################


class PatientManager:

    # create a list of patients and populate it from the patients.txt
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # format patient object just like in the file
    def format_patient_info_for_file(self, patient):
        return f"{patient.get_pid()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}"

    # ask user for info to enter new patient
    def enter_patient_info(self):
        pid = input("Enter Patient id: ")
        name = input("Enter Patient name: ")
        disease = input("Enter Patient disease: ")
        gender = input("Enter Patient gender: ")
        age = input("Enter Patient age: ")
        print()
        return Patient(pid, name, disease, gender, age)

    # reads patients.txt to get a list of patients. This file is separated by underscores
    def read_patients_file(self):
        with open("patients.txt", "r") as file:
            # skip the header line
            next(file)
            for line in file:
                patient_info = line.strip().split("_")
                self.patients.append(Patient(patient_info[0], patient_info[1], patient_info[2], patient_info[3], patient_info[4]))

    # search for a patient in the patients list by id. If it is found print it
    def search_patient_by_id(self):
        patient_id = input("Enter the Patient Id: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                print("{:<10} {:<20} {:<15} {:<15} {:<15}\n".format(
                    "Id", "Name", "Disease", "Gender", "Age"))
                print(self.display_patient_info(patient))
                return
        print("Can't find the Patient with the same id on the system\n")

    # display one patient object in fixed width fields like a table
    def display_patient_info(self, patient):
        return ("{:<10} {:<20} {:<15} {:<15} {:<15}\n".format(
            patient.get_pid(), patient.get_name(), patient.get_disease(), patient.get_gender(), patient.get_age()))

    # edit the patient in the patients list and also update the patient.txt file
    def edit_patient_info_by_id(self):
        patient_id = input("Please enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                patient.set_name(input("Enter new Name: "))
                patient.set_disease(input("Enter new disease: "))
                patient.set_gender(input("Enter new gender: "))
                patient.set_age(input("Enter new age: "))
                print()
                self.write_list_of_patients_to_file()
                print(f"Patient whose ID is {patient_id} has been edited.\n")
                return
        print("Can't find the Patient with the same id on the system\n")

    # displays a list of patients by calling the display_patient_info in a loop
    def display_patients_list(self):

        print("{:<10} {:<20} {:<15} {:<15} {:<15}\n".format(
            "Id", "Name", "Disease", "Gender", "Age"))
        for patient in self.patients:
            print(self.display_patient_info(patient))

    # writes list of patients to the file. Gets formatted line from format_patient_info_for_file() and writes each line
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write("\n" + self.format_patient_info_for_file(patient))

    # appends new patients to the end of file
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        formatted_patient_info = self.format_patient_info_for_file(new_patient)
        with open("patients.txt", "a") as file:
            file.write(formatted_patient_info + "\n")
        print(f"Patient whose ID is {new_patient.get_pid()} has been added.\n")


################################################################################

class Management:
    # create doctor and patient managers

    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("Welcome to Alberta Hospital (AH) Management system")
            print("Select from the following options, or select 3 to stop:")
            print("1 - \tDoctors")
            print("2 - \tPatients")
            print("3 - \tExit Program")
            choice = input()
            print()

            if choice == "1":
                while True:
                    print("Doctors Menu:")
                    print("1 - Display Doctors list")
                    print("2 - Search for doctor by ID")
                    print("3 - Search for doctor by name")
                    print("4 - Add doctor")
                    print("5 - Edit doctor info")
                    print("6 - Back to the Main Menu")
                    choice = input()
                    print()

                    if choice == "1":
                        self.doctor_manager.display_doctors_list()
                    elif choice == "2":
                        self.doctor_manager.search_doctor_by_id()
                    elif choice == "3":
                        self.doctor_manager.search_doctor_by_name()
                    elif choice == "4":
                        self.doctor_manager.add_dr_to_file()
                    elif choice == "5":
                        self.doctor_manager.edit_doctor_info()
                    elif choice == "6":
                        break
                    else:
                        print("Invalid input. Please try again.\n")

            elif choice == "2":
                while True:
                    print("Patients Menu:")
                    print("1 - Display Patients list")
                    print("2 - Search for patient by ID")
                    print("3 - Add patient")
                    print("4 - Edit patient info")
                    print("5 - Back to the Main Menu")
                    choice = input("")
                    print()

                    if choice == "1":
                        self.patient_manager.display_patients_list()
                    elif choice == "2":
                        self.patient_manager.search_patient_by_id()
                    elif choice == "3":
                        self.patient_manager.add_patient_to_file()
                    elif choice == "4":
                        self.patient_manager.edit_patient_info_by_id()
                    elif choice == "5":
                        break
                    else:
                        print("Invalid input. Please try again.\n")

            elif choice == "3":
                print("Thanks for using the program. Bye!\n")
                break

            else:
                print("Invalid input. Please try again.\n")


#############################################################

# create an instance of Management class and run the program
management_system = Management()

# display the menu
management_system.display_menu()
