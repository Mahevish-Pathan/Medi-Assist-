import streamlit as st

def render_history():

    st.subheader("📝 Chat History")

    search_text = st.text_input(
        "Search Question",
        key="history_search"
    )

    for index, msg in enumerate(st.session_state.messages):

        if msg["role"] == "user":

            question = msg["content"]

            if search_text.lower() in question.lower():

                if st.button(
                    question,
                    key=f"history_{index}"
                ):

                    st.session_state["selected_question"] = index

    st.divider()

    if st.button("🗑 Clear Chat History"):

       if st.button(question):
        st.session_state["selected_question"] = index

        st.rerun()