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