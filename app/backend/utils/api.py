import requests

BACKEND_URL = "http://127.0.0.1:8000"


def upload_pdf(files):

    return requests.post(
        f"{BACKEND_URL}/upload",
        files=files
    )


def ask_question(question):

    return requests.post(
        f"{BACKEND_URL}/chat",
        json={
            "query": question
        }
    )