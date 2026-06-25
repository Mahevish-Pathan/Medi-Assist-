from app.backend.mcp_client import (
    get_patient_history,
    get_lab_results,
    get_payment_summary,
    search_patients
)


def handle_mcp_query(query):

    query = query.lower()

    if "patient history" in query:

        patient_id = query.split()[-1]

        return get_patient_history(patient_id)

    elif "lab result" in query:

        patient_id = query.split()[-1]

        return get_lab_results(patient_id)

    elif "payment" in query:

        patient_id = query.split()[-1]

        return get_payment_summary(patient_id)

    elif "search patient" in query:

        name = query.replace(
            "search patient",
            ""
        ).strip()

        return search_patients(name)

    return None