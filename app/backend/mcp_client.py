import requests

MCP_URL = "http://127.0.0.1:9000"


def get_patient_history(patient_id):

    response = requests.get(
        f"{MCP_URL}/patient-history/{patient_id}"
    )

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    return response.text

def get_lab_results(patient_id):

    response = requests.get(
        f"{MCP_URL}/lab-results/{patient_id}"
    )

    return response.json()


def get_payment_summary(patient_id):
    response = requests.get(
        f"{MCP_URL}/patient-history/{patient_id}"
        )
    print("Status:", response.status_code)
    print("Response:", response.text)
    return response.json()

def search_patients(name):

    response = requests.get(
        f"{MCP_URL}/search-patient/{name}"
    )

    return response.json()