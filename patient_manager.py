from patient import Patient

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
