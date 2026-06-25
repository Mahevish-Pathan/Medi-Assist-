import streamlit as st
import requests

from components.source import show_sources

BACKEND_URL = "http://127.0.0.1:8000"


def render_chat():

    st.subheader("💬 MediAssist Chat")

    # ----------------------------------
    # Show Selected Conversation
    # ----------------------------------

    if (
        st.session_state.get("selected_question") is not None
        and isinstance(
            st.session_state["selected_question"],
            int
        )
    ):

        q_index = st.session_state["selected_question"]

        if q_index < len(st.session_state.messages):

            st.info("📌 Selected Conversation")

            with st.container():

                st.chat_message("user").markdown(
                    st.session_state.messages[q_index]["content"]
                )

                if q_index + 1 < len(st.session_state.messages):

                    st.chat_message("assistant").markdown(
                        st.session_state.messages[q_index + 1]["content"]
                    )

                    if (
                        "sources"
                        in st.session_state.messages[q_index + 1]
                    ):

                        show_sources(
                            st.session_state.messages[q_index + 1]["sources"]
                        )

            st.divider()

    # ----------------------------------
    # Full Chat Conversation
    # ----------------------------------

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )

            if (
                message["role"] == "assistant"
                and "sources" in message
                and len(message["sources"]) > 0
            ):

                show_sources(
                    message["sources"]
                )

    # ----------------------------------
    # User Input
    # ----------------------------------

    user_question = st.chat_input(
        "Ask a medical question..."
    )

    if user_question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_question
            }
        )

        try:

            response = requests.post(
                f"{BACKEND_URL}/chat",
                json={
                    "query": user_question
                }
            )

            data = response.json()

            answer = data.get(
                "answer",
                "No answer received."
            )

            source_list = []

            if "sources" in data:

                for source in data["sources"]:

                    file_name = source.get(
                        "file",
                        "Unknown"
                    )

                    page = source.get(
                        "page",
                        "N/A"
                    )

                    source_list.append(
                        f"{file_name} (Page {page})"
                    )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "sources": source_list
                }
            )

        except Exception as e:

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": f"Error: {str(e)}",
                    "sources": []
                }
            )

        st.rerun()