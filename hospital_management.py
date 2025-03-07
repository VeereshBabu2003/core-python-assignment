def search_by_disease(patients, disease):
    """Returns names of patients with the specified disease."""
    return [patient["Name"] for patient in patients if patient["Disease"] == disease]

# Example Input
patients = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]
print("Patients with Flu:", search_by_disease(patients, "Flu"))
