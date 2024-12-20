class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Disease: {self.disease}"

def display_patients(patients):
    if patients:
        print("Patient Records:")
        for patient in patients:
            print(f"Name: {patient['Name']}, Age: {patient['Age']}, Disease: {patient['Disease']}")
    else:
        print("No patient records to display.")

def search_patients_by_disease(patients, disease):
    return [patient['Name'] for patient in patients if patient['Disease'] == disease]

patients = []
num_patients = int(input("Enter the number of patients: "))
for _ in range(num_patients):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter patient disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})
display_patients(patients)
search_disease = input("Enter the disease to search for: ")
result = search_patients_by_disease(patients, search_disease)
print(f"Patients with {search_disease}: {result}")
