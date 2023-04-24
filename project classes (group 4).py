# Define the Doctor class with its properties LMAO
class Doctor:
    def __init__(self, id=None, name=None, speciality=None, timing=None, qualification=None, room=None):
        # Initialize the doctor object properties
        self.id = id
        self.name = name
        self.speciality = speciality
        self.timing = timing
        self.qualification = qualification
        self.room = room

    # Getters
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_speciality(self):
        return self.speciality

    def get_timing(self):
        return self.timing

    def get_qualification(self):
        return self.qualification

    def get_room(self):
        return self.room

    # Setters
    def set_id(self, new_id):
        self.id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_speciality(self, new_speciality):
        self.speciality = new_speciality

    def set_timing(self, new_timing):
        self.timing = new_timing

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room(self, new_room):
        self.room = new_room

    # String representation of the doctor object
    def __str__(self):
        return str(self.id) + '_' + self.name + '_' + self.speciality + '_' + self.timing + '_' + self.qualification + '_' + str(self.room)


# Define the DoctorManager class with its methods
class DoctorManager:
    def __init__(self):
        # Create an empty list to hold doctors
        self.doctors_list = []
        # Call read_doctors_file method to load data from file into the list
        self.read_doctors_file()

    # Method to format a doctor's information in the same format as in the data file
    def format_dr_info(self, dr):
        return str(dr.id) + '_' + dr.name + '_' + dr.speciality + '_' + dr.timing + '_' + dr.qualification + '_' + str(dr.room)

    # Method to get doctor information from user and create a doctor object
    def enter_dr_info(self):
        # Prompt user to enter doctor info
        dr_id = input('Enter doctor ID: ')
        name = input('Enter doctor name: ')
        speciality = input('Enter doctor speciality: ')
        timing = input('Enter doctor timing: ')
        qualification = input('Enter doctor qualification: ')
        room = input('Enter doctor room: ')
        # Create a new doctor object using the entered information
        new_dr = Doctor(dr_id, name, speciality, timing, qualification, room)
        # Return the new doctor object
        return new_dr

    # Method to read doctor information from the data file and populate the list
    def read_doctors_file(self):
        # Open the data file
        with open('doctors.txt', 'r') as f:
            # Iterate over each line in the file
            for line in f:
                # Split the line into its component properties
                dr_props = line.strip().split('_')
                # Create a new Doctor object using the properties
                new_dr = Doctor(dr_props[0], dr_props[1], dr_props[2], dr_props[3], dr_props[4], dr_props[5])
                # Add the new doctor object to the doctors list
                self.doctors_list.append(new_dr)

    # Method to search for a doctor by their ID
    def search_doctor_by_id(self):
        # Prompt user to enter doctor ID
        dr_id = input('Enter doctor ID: ')
        # Iterate over each doctor in the list
        for dr in self.doctors_list:
            # Check if the current doctor's ID matches the entered ID
            if dr.id == dr_id:
                # If a match is found, display the doctor's information and return True
                print(self.format_dr_info(dr))
                return True
        # If no match is found, display an error message and return False
        print('Can’t find the doctor...')
        return False

    # Method to search for a doctor by their name
    def search_doctor_by_name(self):
        # Prompt user to enter doctor name
        dr_name = input('Enter doctor name: ')
        # Iterate over each doctor in the list
        for dr in self.doctors_list:
            # Check if the current doctor's name matches the entered name
            if dr.name.lower() == dr_name.lower():
                # If a match is found, display the doctor's information and return True
                print(self.format_dr_info(dr))
                return True
        # If no match is found, display an error message and return False
            print('Can’t find the doctor...')
            return False

# Method to add a new doctor to the list
    def add_doctor(self):
        # Call enter_dr_info method to get new doctor information
        new_dr = self.enter_dr_info()
        # Append the new doctor object to the doctors list
        self.doctors_list.append(new_dr)
        # Display a success message
        print('Doctor added successfully!')

    # Method to delete a doctor from the list by their ID
    def delete_doctor(self):
        # Prompt user to enter doctor ID
        dr_id = input('Enter doctor ID: ')
        # Iterate over each doctor in the list
        for dr in self.doctors_list:
            # Check if the current doctor's ID matches the entered ID
            if dr.id == dr_id:
                # If a match is found, remove the doctor object from the list and display a success message
                self.doctors_list.remove(dr)
                print('Doctor deleted successfully!')
                return True
        # If no match is found, display an error message and return False
        print('Can’t find the doctor...')
        return False

    # Method to update a doctor's information in the list by their ID
    def update_doctor(self):
        # Prompt user to enter doctor ID
        dr_id = input('Enter doctor ID: ')
        # Iterate over each doctor in the list
        for dr in self.doctors_list:
            # Check if the current doctor's ID matches the entered ID
            if dr.id == dr_id:
                # If a match is found, prompt user to enter updated information
                name = input('Enter updated doctor name: ')
                speciality = input('Enter updated doctor speciality: ')
                timing = input('Enter updated doctor timing: ')
                qualification = input('Enter updated doctor qualification: ')
                room = input('Enter updated doctor room: ')
                # Update the doctor object with the new information
                dr.name = name
                dr.speciality = speciality
                dr.timing = timing
                dr.qualification = qualification
                dr.room = room
                # Display a success message
                print('Doctor information updated successfully!')
                return True
        # If no match is found, display an error message and return False
        print('Can’t find the doctor...')
        return False

    # Method to save the updated doctor list to the data file
    def save_doctors_file(self):
        # Open the data file in write mode
        with open('doctors.txt', 'w') as f:
            # Iterate over each doctor in the list
            for dr in self.doctors_list:
                # Write the formatted doctor information to the file
                f.write(self.format_dr_info(dr) + '\n')
        # Display a success message
        print('Doctor information saved to file successfully!')

class Patient:
    # Represents a patient with a unique id, name, disease, gender, and age.

    def __init__(self, pid="", name="", disease="", gender="", age=0):
        # Initializes a patient object with the given properties.
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        # Returns the patient id.
        return self.pid

    def set_pid(self, new_pid):
        # Sets the patient id to a new value.
        self.pid = new_pid

    def get_name(self):
        # Returns the patient name.
        return self.name

    def set_name(self, new_name):
        # Sets the patient name to a new value.
        self.name = new_name

    def get_disease(self):
        # Returns the patient's disease.
        return self.disease

    def set_disease(self, new_disease):
        # Sets the patient's disease to a new value.
        self.disease = new_disease

    def get_gender(self):
        # Returns the patient's gender.
        return self.gender

    def set_gender(self, new_gender):
        # Sets the patient's gender to a new value.
        self.gender = new_gender

    def get_age(self):
        # Returns the patient's age.
        return self.age

    def set_age(self, new_age):
        # Sets the patient's age to a new value.
        self.age = new_age

    def __str__(self):
        # Returns a string representation of the patient object.
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"

class PatientManager:
    # Initializes the list of patients and reads patient information from a file
    def __init__(self):
        self.patients = []
        self.read_patients_file()

    # Format the patient information for the file
    def format_patient_info_for_file(self, patient):
        return f"{patient.get_pid()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}\n"

    # Prompt the user to enter patient information and return a new Patient object
    def enter_patient_info(self):
        pid = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        return Patient(pid=pid, name=name, disease=disease, gender=gender, age=age)

    # Read patient information from a file and store it in the list of patients
    def read_patients_file(self):
        with open("patients.txt", "r") as file:
            for line in file:
                pid, name, disease, gender, age = line.strip().split("_")
                self.patients.append(Patient(pid=pid, name=name, disease=disease, gender=gender, age=age))

    # Search for a patient by ID and display their information
    def search_patient_by_id(self):
        pid = input("Enter patient ID: ")
        for patient in self.patients:
            if patient.get_pid() == pid:
                self.display_patient_info(patient)
                return
        print("Can't find the patient...")

    # Display the list of patients and their information
    def display_patient_info(self, patient):
        print(f"Patient ID: {patient.get_pid()}")
        print(f"Name: {patient.get_name()}")
        print(f"Disease: {patient.get_disease()}")
        print(f"Gender: {patient.get_gender()}")
        print(f"Age: {patient.get_age()}")

    # Edit patient information by ID
    def edit_patient_info_by_id(self):
        pid = input("Enter patient ID: ")
        for patient in self.patients:
            if patient.get_pid() == pid:
                name = input("Enter new patient name: ")
                disease = input("Enter new patient disease: ")
                gender = input("Enter new patient gender: ")
                age = input("Enter new patient age: ")
                patient.set_name(name)
                patient.set_disease(disease)
                patient.set_gender(gender)
                patient.set_age(age)
                self.write_list_of_patients_to_file()
                print("Patient information has been updated.")
                return
        print("Cannot find the patient...")

    # Display the list of patients and their information
    def display_patients_list(self):
        for patient in self.patients:
            self.display_patient_info(patient)
            print()

    # Write the list of patients to a file
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient))

    # Add a new patient to the file and list of patients
    def add_patient_to_file(self):
        patient = self.enter_patient_info()
        self.patients.append(patient)
        with open("patients.txt", "a") as file:
            file.write(self.format_patient_info_for_file(patient))
        print("A new patient has been added.")
    
class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        # Displays the main menu and takes input from the user until the user enters 3 to exit the program
        while True:
            print("Main Menu:")
            print("1. Doctors")
            print("2. Patients")
            print("3. Exit Program")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display_doctor_menu()
            elif choice == "2":
                self.display_patient_menu()
            elif choice == "3":
                print("Exiting program...")
                break
            else:
                print("Invalid choice, please try again.")

    def display_doctor_menu(self):
        # Displays the doctor menu and takes input from the user until the user enters 6 to return to the main menu
        while True:
            print("Doctor Menu:")
            print("1. Display list of doctors")
            print("2. Search doctor by ID")
            print("3. Search doctor by name")
            print("4. Add new doctor")
            print("5. Edit existing doctor information")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.doctor_manager.display_doctors_list()
            elif choice == "2":
                self.doctor_manager.search_doctor_by_id()
            elif choice == "3":
                self.doctor_manager.search_doctor_by_name()
            elif choice == "4":
                self.doctor_manager.add_doctor_to_file()
            elif choice == "5":
                self.doctor_manager.edit_doctor_info_by_id()
            elif choice == "6":
                break
            else:
                print("Invalid choice, please try again.")

    def display_patient_menu(self):
        # Displays the patient menu and takes input from the user until the user enters 5 to return to the main menu
        while True:
            print("Patient Menu:")
            print("1. Display list of patients")
            print("2. Search patient by ID")
            print("3. Add new patient")
            print("4. Edit existing patient information")
            print("5. Back to Main Menu")
            choice = input("Enter your choice: ")
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
                print("Invalid choice, please try again.")